
# CSV Files Merging Script

This script is designed to merge multiple CSV files that start with "data_" and are located in a specified directory. It uses the Pandas library to read, process, and concatenate the CSV files, resulting in a single merged CSV file.

What's different from other codes?
> This one only keep the header from the first file. It is intended to use when multiple similar files should be merged.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your machine.
- Pandas library installed. You can install it using the following command:
  ```
  pip install pandas
  ```

## Usage

1. Place all the CSV files you want to merge in a directory.
2. Open the script file `merge_csv_files.py` in a text editor or an integrated development environment (IDE) of your choice.
3. Modify the `dir_path` variable to the path of the directory containing your CSV files.
4. Run the script using the following command:
   ```
   python merge_csv_files.py
   ```
5. After the script finishes running, a new CSV file named `all_data_merged.csv` will be created in the same directory as your input files. This file will contain the merged data from all the input CSV files.

## Important Notes

- Ensure that your CSV files have the same structure and column names for successful merging.
- The script assumes that the CSV files are using semicolon (`;`) as the separator and comma (`.`) as the decimal point. If your files use a different separator or decimal point, you may need to adjust the `sep` and `decimal` parameters in the script.
- The merged CSV file will not include any index columns from the original CSV files.

_________________



# Text File Merger using Tkinter

This script is designed to merge the contents of multiple text files (`.txt`) into a single file named `merged.txt`. It utilizes the Tkinter library to create a file dialog for the user to select multiple input text files. The contents of the selected files are then merged and written into the output file.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your machine.

## Usage

1. Open the script file `merge_text_files.py` in a text editor or an integrated development environment (IDE) of your choice.
2. Run the script using the following command:
   ```
   python merge_text_files.py
   ```
3. A file dialog will open, allowing you to select one or more text files that you want to merge.
4. After selecting the files, the script will merge their contents and create a file named `merged.txt` in the same directory as the script.

## Important Notes

- The script filters for files with the `.txt` extension in the file dialog, but you can modify the filetypes in the `filedialog.askopenfilenames()` function call to select files with different extensions.
- The merged content is written to a file named `merged.txt` in the same directory as the script. If you want to change the output file name or location, you can modify the `output_file` variable.
- The Tkinter window is briefly displayed to open the file dialog and then immediately closed after selections are made.
