# functions that intake rows and output based on value
# 
import pandas as pd
import re

# function to delete rows based on regex string and type of variable
# takes a dataframe, the column to search, and a regex matcher
# this will be used to detect if the LSOA column contains valid LSOA strings 
def delete_rows_by_regex(dataframe, col_num, matcher):
    rows_to_delete = [] # empty list to append rows
    for index, row in dataframe.iterrows(): # loop through the dataframe
        row_var = row[col_num] # find the value in the relevant column
        if type(row_var) is not str: # check if type is string
            rows_to_delete.append(index) # if type is not string append to rows_to_delete
        else:
            if not bool(re.search(matcher, row_var)): # search for the regex (i.e. LSOA)
                rows_to_delete.append(index)

    return rows_to_delete


# function that returns the index of a dataframe based on the first occurence of a string
# takes dataframe, column to search and matcher as a string
# returns index (type = int)
def find_row_index(dataframe, col_num, matcher):
    dataframe_length = len(dataframe) # length of df, used to detect if reached the end without match
    for index, row in dataframe.iterrows(): # loop over rowss
        if row[col_num] == matcher:
            return index
        elif index == dataframe_length - 1:
            print(matcher + "... not found")
            return False


# function to create a date for each month (01/XX/YEAR)
# takes a year as a string
def create_monthly_dates(year):
    month_array = []
    for m in range(1, 13, 1):
        date_string = "01-{}-{}".format(m, year)
        month_array.append(date_string)

    return month_array