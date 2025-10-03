# util.py
import json
import pickle
import numpy as np
import os

# Globals
__locations = None
__data_columns = None
__model = None

# Load saved model and data columns
def load_saved_artifacts():
    print("✅ Loading saved artifacts...")
    global __data_columns
    global __locations
    global __model

    base_path = os.path.join(os.path.dirname(__file__), '.venv', 'artifacts')

    # Load data columns
    with open(os.path.join(base_path, "colums.json"), "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # Skip total_sqft, bath, bhk

    # Load trained model
    with open(os.path.join(base_path, "banglore_home_prices_model.pickle"), "rb") as f:
        __model = pickle.load(f)

    print("✅ Artifacts loaded successfully.")

# Predict home price
def get_estimated_price(location, sqft, bhk, bath):
    if __model is None or __data_columns is None:
        raise Exception("Artifacts not loaded. Call load_saved_artifacts() first.")

    location = location.strip().lower()
    try:
        loc_index = [col.lower() for col in __data_columns].index(location)
    except ValueError:
        loc_index = -1  # location not found

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

# Get all locations
def get_location_names():
    if __locations is None:
        raise Exception("Artifacts not loaded. Call load_saved_artifacts() first.")
    return __locations

# Get all column names
def get_data_columns():
    if __data_columns is None:
        raise Exception("Artifacts not loaded. Call load_saved_artifacts() first.")
    return __data_columns
