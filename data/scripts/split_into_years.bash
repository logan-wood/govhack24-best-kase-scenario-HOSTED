#!/bin/bash

# Check if the CSV file is passed as an argument
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <csv_file>"
  exit 1
fi

input_file="$1"

# Read the header (first line) of the CSV file
header=$(head -n 1 "$input_file")

# Loop through each row in the CSV, skipping the header
tail -n +2 "$input_file" | while IFS=',' read -r accident_no accident_date accident_time accident_type accident_type_desc day_of_week day_week_desc dca_code dca_desc light_condition node_id no_of_vehicles no_persons_killed no_persons_inj_2 no_persons_inj_3 no_persons_not_inj no_persons police_attend road_geometry road_geometry_desc severity speed_zone rma; do
  # Extract the year from the ACCIDENT_DATE (format YYYY-MM-DD)
  year=$(echo "$accident_date" | cut -d '-' -f 1)
  
  # Check if the file for the year already exists, if not, create it with the header
  if [ ! -f "${year}.csv" ]; then
    echo "$header" > "${year}.csv"
  fi
  
  # Append the current row to the respective year file
  echo "$accident_no,$accident_date,$accident_time,$accident_type,$accident_type_desc,$day_of_week,$day_week_desc,$dca_code,$dca_desc,$light_condition,$node_id,$no_of_vehicles,$no_persons_killed,$no_persons_inj_2,$no_persons_inj_3,$no_persons_not_inj,$no_persons,$police_attend,$road_geometry,$road_geometry_desc,$severity,$speed_zone,$rma" >> "${year}.csv"
done

echo "CSV split into files based on the year of ACCIDENT_DATE."

