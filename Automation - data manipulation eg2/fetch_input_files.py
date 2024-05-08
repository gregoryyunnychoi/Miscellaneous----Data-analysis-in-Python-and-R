# functions which takes in folder location and returns a list of all files in that folder

import pandas as pd
import os

# def generate_soure_path(user_name, source_type, source_name):

# takes source folder (e.g. BRES/raw_inputs) and optional file type (e.g. csv, xlsx). 
# if file type not specified returns all files
# returns list of file names 
def fetch_input_files_list(source_folder, file_type=False):
    print("fetching files ...")
    file_list = [] # empty list to append outputs
    for file in os.listdir(source_folder): # loop through all files in the source folder
        if file_type: # if there is a file type specified
            if file.endswith(file_type): # take only the files that end with that type (e.g. CSVs)
                file_list.append(file)
        else: # if there is no file type specified just output all files in that folder
            file_list.append(file)
    
    return file_list

# takes user name (as string) and outputs correct path to connect to sharepoint
# returns a string with the absolute path of the dashboard / Data sharepoint folder on the user's machine
def find_input_path(user_name):
    folder_base = fr"C:\Users\{user_name}\Documents\GitHub\miscellaneous\Automation - data manipulation eg2"
    # Check if the path actually exists
    if not os.path.exists(folder_base):
        return "Directory does not exist"
    return folder_base

   
