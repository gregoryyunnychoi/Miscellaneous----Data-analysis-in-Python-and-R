## Repository Overview

This repository contains the re-creation of the examples of my previous work in data manipulation and data analysis in Python and R using public data.

### Folder Descriptions

#### Example 1 - Automating Data Manipulation 
This folder demonstrates in R how to:
- Manipulate a single CSV file.
- Loop over a folder full of CSV files with the same data structure.

We process our data in the `/Before` folder and then export the modified files, named "_done.csv", into the `/Before/test` folder. The script used is `Automating_Data_manipulation.r`. Please update the path to your working directory using `getwd()`.

#### Example 2 - Automating Data Manipulation 
This folder demonstrates a Python-based data manipulation process similar to Example 1, using Scottish employment data from NOMIS. The scripts used are `Script 1.py` and `Script 2.py`. We begin with "Raw data", then store the processed data in the "Step 1" folder, and finally combine them using the concatenate function. The final results are stored in the "Final" folder.

#### Example 3 - Problem-solving: How many combination there is to build a stadium allowed for more than 42k seats 
This is a problem I encountered during my time as an Economic Consultant at Arup. The data and content have been altered for confidentiality reasons.

Imagine you are tasked with designing a football stadium where there are various types of stands to choose from. Each type of stand offers a certain number of options, and each option contains a specific number of seats. For example, Type 1 stands have 13 different options, with each option containing _x_ number of seats; Type 2 stands have 3 options, with each option containing _y_ number of seats, and so on.

The question is: how many combinations are there to arrange the stands, given the condition that the stadium must have at least 42,000 seats?

To solve this, I wrote an algorithm that loops through all possible combinations, counting only those that meet or exceed the condition of 42,000 seats.
