import os
import pandas as pd

# Directory where CSV files are stored
dir_path = r"C:\Users\gbray\Desktop\python\project 2\data"

# List to store dataframes
df_list = []

# Get a list of all files in the directory
file_list = os.listdir(dir_path)

# Filter and process only CSV files that start with "data_"
for file in file_list:
    if file.startswith("data_") and file.endswith(".csv"):
        file_path = os.path.join(dir_path, file)
        # Read CSV file into DataFrame and add to list
        df = pd.read_csv(file_path, sep=';', decimal=',')
        df_list.append(df)

# Concatenate all dataframes
df_all = pd.concat(df_list, ignore_index=True)

# Save the merged data to a new CSV file
output_file = os.path.join(dir_path, 'all_data_merged.csv')
df_all.to_csv(output_file, index=False)

print(f"Merged all CSV files into {output_file}")
