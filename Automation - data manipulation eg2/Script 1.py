# -*- coding: utf-8 -*-
import pandas as pd
import os
import math
import csv

# Get the path to the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))#This is quite a cool script.
base_folder = script_directory
folder_location = base_folder + r"\b_data"
input_folder = folder_location + r'\Raw data'

input_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

output_folder = folder_location + '\\Step 1'

#input_file = '121427955680904_2SIC_2016.csv'

for input_file in input_files:

    # set up import statements
    loaded_file = []
    file_path = os.path.join(input_folder, input_file)
    print(f"processing .... {input_file}")

    # use csv loader instead of the read_csv pandas function
    # this method is less strict on the formatting of the csv
    # meaning it can better handle the meta data in the file (you can find this on Youtube)
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            loaded_file.append(row)
    
    input_df = pd.DataFrame(loaded_file) # transform loaded file into a pandas dataframe
    column_names = list(input_df)

    # find the row with column headings (due to blank space at the top of the BRES input data)
    headings_row = input_df.loc[input_df[0] == "2011 scottish datazone"].values.flatten().tolist()
    # grab year 
    year_var = input_df.loc[input_df[0] == "Date       :"].values.flatten().tolist()[1]
    # grab measure 
    measure_var = input_df.loc[input_df[0] == "measure    :"].values.flatten().tolist()[1]
    # grab variable 
    variable_var = input_df.loc[input_df[0] == "Employment status:"].values.flatten().tolist()[1]

    # keep only rows that match LSOA regex
    list_rows_to_delete = input_df[~input_df[0].str.match(r'[a-zA-Z]{1}\d{8}', na = False)].index.tolist() # the ~ is to invert the boolean. This is quite important!
    # print(list_rows_to_delete)
    input_df = input_df.drop(input_df.index[list_rows_to_delete])

    input_df.columns = headings_row

    # remove unlabbelled columns
    column_names = list(input_df)
    columns_to_delete = []
    columns_to_delete = [index for index, col in enumerate(column_names) if col == ""]    
    input_df = input_df.drop(input_df.columns[columns_to_delete], axis=1) # 

    # split first cell into LSOA and LSOA name and 
    input_df[['Data_zone', 'Data_zone_name']] = input_df['2011 scottish datazone'].str.split(' : ', expand=True)
    input_df = input_df.drop('2011 scottish datazone', axis=1)
    # set year column 
    input_df['year'] = year_var
    
    # save to processed files 
    input_file_name = input_file[:len(input_file)-4] # take the file name of the input (but remove the '.csv' at the end of the string)
    processed_file_meta = [str(variable_var), input_file_name] # create a name for the processed file 
    processed_file_name = '-'.join(processed_file_meta) # create a string to save the file as
    input_df.to_csv(f'{output_folder}/{processed_file_name}.csv', index=False)
    print(f"processed .... {processed_file_name}.csv")


####################
