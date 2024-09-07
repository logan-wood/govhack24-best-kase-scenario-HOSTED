#!/bin/bash

# Input file paths
geojson_file="VICTORIAN_ROAD_CRASH_DATA.geojson"
csv_file="WOMBATS.csv"
output_file="WOMBAT_locations.csv"

# Create an associative array to store ACCIDENT_NO from WOMBAT.csv
declare -A accident_ids

# Read IDs from WOMBAT.csv and store them in the associative array
while IFS=',' read -r accident_no; do
  accident_ids["$accident_no"]=1
done < "$csv_file"

# Initialize the output CSV with headers
echo "ACCIDENT_NO,LONGITUDE,LATITUDE" > "$output_file"

# Use 'jq' to process the GeoJSON file one object at a time
jq -c '.features[]' "$geojson_file" | while read -r feature; do
  # Extract ACCIDENT_NO and the coordinates (longitude and latitude) from the current JSON feature
  accident_no=$(echo "$feature" | jq -r '.properties.ACCIDENT_NO')
  longitude=$(echo "$feature" | jq -r '.geometry.coordinates[0]')
  latitude=$(echo "$feature" | jq -r '.geometry.coordinates[1]')
  
  # Check if ACCIDENT_NO is in the associative array (exists in WOMBAT.csv)
  if [[ ${accident_ids["$accident_no"]+_} ]]; then
    # Output ACCIDENT_NO, LONGITUDE, and LATITUDE to WOMBAT_locations.csv
    echo "$accident_no,$longitude,$latitude" >> "$output_file"
  fi
done

echo "Filtered locations saved to $output_file"

