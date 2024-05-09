## Repository Overview

This repository contains the re-creation of the examples of my previous work in data manipulation and data analysis in Python and R using public data.

### Folder Descriptions

#### Automating Data Manipulation Example 1
This folder demonstrates in R how to:
- Manipulate a single CSV file.
- Loop over a folder full of CSV files with the same data structure.

We process our data in the `/Before` folder and then export the modified files, named "_done.csv", into the `/Before/test` folder. The script used is `Automating_Data_manipulation.r`. Please update the path to your working directory using `getwd()`.

#### Automating Data Manipulation Example 2
This folder demonstrates a Python-based data manipulation process similar to Example 1, using Scottish employment data from NOMIS. The scripts used are `Script 1.py` and `Script 2.py`. We begin with "Raw data", then store the processed data in the "Step 1" folder, and finally combine them using the concatenate function. The final results are stored in the "Final" folder.

