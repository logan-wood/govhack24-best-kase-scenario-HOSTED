import pandas as pd

# Read the two CSV files

csv1 = pd.read_csv('ACCIDENT.csv')
csv2 = pd.read_csv('rearranged.csv')
csv3 = pd.read_csv('pyth_merged_file.csv')
csv4 = pd.read_csv('rearranged.csv')


# Merge the two dataframes on the 'ID' column
merged_df = pd.merge(csv1, csv2, on='ACCIDENT_NO', how='inner')

# Drop duplicates if they exist
merged_df = merged_df.drop_duplicates(subset='ACCIDENT_NO')

# Save the resulting dataframe to a new CSV
merged_df.to_csv('pyth_merged_file2.csv', index=False)

print("Merged CSV saved without duplicates.")


ROAD_SURFACE_COND.csv
