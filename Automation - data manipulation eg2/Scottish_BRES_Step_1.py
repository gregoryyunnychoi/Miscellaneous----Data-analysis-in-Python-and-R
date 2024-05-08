# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:51:20 2023

@author: Gregory.Choi
"""
import pandas as pd
import os
import re
import math
import csv

from fetch_input_files import fetch_input_files_list, find_input_path
from row_manipulation import delete_rows_by_regex

    # declare location of raw inputs

user_name = os.getlogin()
base_folder = find_input_path(user_name)
folder_location = base_folder + r"\BRES_Scot"
input_folder = folder_location + '/Raw data'

input_files = fetch_input_files_list(input_folder, file_type='csv')

output_folder = folder_location + '\\Processed data'

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

    # To be moved to Pytest...
    #   test in the if statement (move to PyTest after reading docs)
    #   test if the first column name is unnamed. 

    # find the row with column headings (due to blank space at the top of the BRES input data)
    headings_row = input_df.loc[input_df[0] == "2011 scottish datazone"].values.flatten().tolist()
    

    # fetch meta data from the top of the csv.
    # This will be useful for naming processed files, and adding variables e.g. year

    # grab year 
    year_var = input_df.loc[input_df[0] == "Date       :"].values.flatten().tolist()[1]
    # grab measure 
    measure_var = input_df.loc[input_df[0] == "measure    :"].values.flatten().tolist()[1]
    # grab variable 
    variable_var = input_df.loc[input_df[0] == "Employment status:"].values.flatten().tolist()[1]

    # keep only rows that match LSOA regex
    list_rows_to_delete = delete_rows_by_regex(input_df, 0, r'[a-zA-Z]{1}\d{8}')
    # print(list_rows_to_delete)
    input_df = input_df.drop(input_df.index[list_rows_to_delete])

    input_df.columns = headings_row

    # remove unlabbelled columns
    column_names = list(input_df)
    columns_to_delete = []

    for index, col in enumerate(column_names): # delete all columns 
        if type(col) == str:
            if 'Unnamed' in col or col == '' or col == 'yes':
                columns_to_delete.append(index)
        elif math.isnan(col):
            columns_to_delete.append(index)
    

    input_df = input_df.drop(input_df.columns[columns_to_delete], axis=1) # 


    # split first cell into LSOA and LSOA name and 
    input_df[['Data_zone', 'Data_zone_name']] = input_df['2011 scottish datazone'].str.split(' : ', expand=True)
    input_df = input_df.drop('2011 scottish datazone', axis=1)
    # set year column based on meta data
    input_df['year'] = year_var
    
    # save to processed files 
    input_file_name = input_file[:len(input_file)-4] # take the file name of the input (but remove the '.csv' at the end of the string)
    #processed_file_meta = [str(year_var), str(variable_var), str(measure_var), input_file_name]
    processed_file_meta = [str(variable_var), input_file_name] # create a name for the processed file with the meta data from the input
    processed_file_name = '-'.join(processed_file_meta) # create a string to save the file as
    input_df.to_csv(f'{output_folder}/{processed_file_name}.csv', index=False)
    print(f"processed .... {processed_file_name}.csv")