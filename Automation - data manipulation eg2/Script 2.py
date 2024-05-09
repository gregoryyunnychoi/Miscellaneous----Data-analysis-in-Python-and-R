import pandas as pd
import os
import re
import glob

# Define the directory path
base_folder =  os.path.dirname(os.path.abspath(__file__))#This is quite a cool script.
directory_path  = base_folder + r'\b_data\Step 1'
output_folder = base_folder + r'\b_data\Final'
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

#We use a simple loop and if condition here to replace : with -
new_column_names = [name.replace(':', '-') if re.match(r'\d{2} : .+', name) else name for name in column_names]

#Using the new column name:
data.columns = new_column_names
print(data)


#Output:
data.to_csv(f'{output_folder}/data.csv', index=False)
