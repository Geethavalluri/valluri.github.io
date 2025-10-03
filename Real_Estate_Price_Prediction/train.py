import pandas as pd
import numpy as np
import json
import pickle
import os
from sklearn.linear_model import LinearRegression

def convert_sqft_to_num(x):
    try:
        tokens = x.split('-')
        if len(tokens) == 2:
            return (float(tokens[0]) + float(tokens[1])) / 2
        return float(x)
    except:
        return None

# Load and clean data
df = pd.read_csv("Bengaluru_House_Data.csv")
df = df.drop(['area_type', 'society', 'balcony', 'availability'], axis=1)
df = df.dropna(subset=['location', 'size', 'total_sqft', 'bath', 'price'])
df['location'] = df['location'].apply(lambda x: x.strip().lower())
df['bhk'] = df['size'].apply(lambda x: int(x.split(' ')[0]) if isinstance(x, str) else None)
df = df[df['bhk'].notnull()]
df['total_sqft'] = df['total_sqft'].apply(convert_sqft_to_num)
df = df[df['total_sqft'].notnull()]

# Group rare locations
location_stats = df['location'].value_counts()
rare_locations = location_stats[location_stats <= 10].index
df['location'] = df['location'].apply(lambda x: 'other' if x in rare_locations else x)

# One-hot encode locations
dummies = pd.get_dummies(df['location'])
df_model = pd.concat([df[['total_sqft', 'bath', 'bhk', 'price']], dummies], axis=1)

X = df_model.drop('price', axis=1)
y = df_model['price']

print(f"Training model with {X.shape[1]} features")  # Should print 243 features

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model and columns
os.makedirs('artifacts', exist_ok=True)

with open('artifacts/banglore_home_prices_model.pickle', 'wb') as f:
    pickle.dump(model, f)

with open('artifacts/colums.json', 'w') as f:
    json.dump({'data_columns': X.columns.tolist()}, f)

print("✅ Model trained and saved to artifacts/")




