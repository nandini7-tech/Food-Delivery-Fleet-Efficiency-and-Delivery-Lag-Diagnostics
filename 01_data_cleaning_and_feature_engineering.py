import pandas as pd
import numpy as np

# 1. Load the training data
df = pd.read_csv('train.csv')

# 2. Fix target variable: strip '(min) ' prefix and convert to numeric
df['Time_taken(min)'] = df['Time_taken(min)'].astype(str).str.replace('(min)', '', regex=False).str.strip()
df['Time_taken(min)'] = pd.to_numeric(df['Time_taken(min)'], errors='coerce')

# 3. Clean string whitespace and replace string 'NaN' with actual nulls
str_cols = df.select_dtypes(include='object').columns
for col in str_cols:
    df[col] = df[col].astype(str).str.strip().replace(['NaN', 'nan'], np.nan)

# Clean column names (standardize Weatherconditions -> Weather_conditions)
df.rename(columns={'Weatherconditions': 'Weather_conditions'}, inplace=True)
df['Weather_conditions'] = df['Weather_conditions'].str.replace('conditions ', '', regex=False)

# 4. Convert numeric fields
numeric_cols = ['Delivery_person_Age', 'Delivery_person_Ratings', 'multiple_deliveries', 'Vehicle_condition']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 5. Calculate Haversine Delivery Distance (km)
def haversine_np(lat1, lon1, lat2, lon2):
    r = 6371.0 # Earth's radius in km
    # Take absolute values to handle negative/inverted GPS coordinate errors
    lat1, lon1, lat2, lon2 = map(np.radians, [np.abs(lat1), np.abs(lon1), np.abs(lat2), np.abs(lon2)])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0)**2
    return 2 * r * np.arcsin(np.sqrt(a))

df['Distance_km'] = haversine_np(
    df['Restaurant_latitude'], df['Restaurant_longitude'],
    df['Delivery_location_latitude'], df['Delivery_location_longitude']
)

# 6. Filter out invalid GPS outliers (e.g. coordinates at 0,0 yielding ~8000+ km)
df = df[(df['Distance_km'] > 0.1) & (df['Distance_km'] < 50)].copy()

# 7. Create Operational KPI Columns
df['Is_Delayed'] = df['Time_taken(min)'].apply(lambda x: 1 if x > 30 else 0)
df['Speed_kmh'] = df['Distance_km'] / (df['Time_taken(min)'] / 60)

# 8. Export the cleaned file for your dashboard/analysis
df.to_csv('cleaned_delivery_data.csv', index=False)
print(f"Data successfully cleaned! Total valid records: {len(df)}")