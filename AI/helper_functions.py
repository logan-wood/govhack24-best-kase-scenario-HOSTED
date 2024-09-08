import pandas as pd
import numpy as np

CSV_FILE_PATH = "../data/pyth_merged_file.csv"

def filter_by_coordinates(lat_min, lat_max, lon_min, lon_max):
    try:
        data = pd.read_csv(CSV_FILE_PATH)
    except FileNotFoundError:
        print("The CSV data file was not found")
        return None
        
    if 'LAT' not in data.columns or 'LONG' not in data.columns:
        print("Dataset must contain 'LAT' and 'LONG' columns.")
        return None

    # Check datatypes, cast if necessary
    print(f"input type: {type(lat_min)}, datasource type {data['LAT'].dtype}")
    lat_min = np.float64(lat_min)
    lat_max = np.float64(lat_max)
    lon_min = np.float64(lon_min)
    lon_max = np.float64(lon_max)

    print(f"checking lat is greater than {lat_min} and smaller than {lat_max}, and checking lon is greater than {lon_min} and smaller than {lon_max}")

    # Filter rows within the specified coordinate bounds
    filtered_data = data[
        (data['LAT'] >= lat_min) &
        (data['LAT'] <= lat_max) &
        (data['LONG'] >= lon_min) &
        (data['LONG'] <= lon_max)
    ]

    print(f"length of data returned: {len(filtered_data)}")

    # for now, return 50
    filtered_data = filtered_data.head(50)

    return filtered_data