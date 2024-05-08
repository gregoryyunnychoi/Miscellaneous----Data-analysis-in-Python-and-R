import pandas as pd
import os
import re
import math
import csv
import glob
from fetch_input_files import find_input_path

# Define the directory path
user_name = os.getlogin()
base_folder = find_input_path(user_name)
directory_path  = base_folder + '\BRES_Scot\Processed data'
output_folder = base_folder + '\BRES_Scot\Transformed data'
all_files = glob.glob(directory_path + "/*.csv")
all_files
#Merge data set
li = []
for filename in all_files:
    df = pd.read_csv(filename, index_col = None, header = 0)
    li.append(df)

data = pd.concat(li, axis = 0)
#change column names
column_names = data.columns


# The string to prepend
prepend_string = "BRES - Total Employed - 2SIC - "

# Function to prepend string to items matching the pattern
def prepend_to_matching_columns(columns, pattern, prepend_str):
    new_columns = []
    for col in columns:
        if re.match(pattern, col):
            new_columns.append(prepend_str + col)
        else:
            new_columns.append(col)
    return new_columns

# The regex pattern for columns starting with two digits, a colon, and a space
pattern = r'\d{2} : .+'

# Applying the function to the column_names and replace ":" for "-".
new_column_names = prepend_to_matching_columns(column_names, pattern, prepend_string)
new_column_names = [col.replace(':', '-') for col in new_column_names]

#Using the new column name:
data.columns = new_column_names
print(data)


#Output:
data.to_csv(f'{output_folder}/data.csv', index=False)
