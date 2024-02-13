# <p align="center">CS2613 Exploratory Assignment</p>
# <p align="center">Caleb Carr</p>
![](https://geo-python-site.readthedocs.io/en/stable/_images/pandas_logo.png)


## Introduction
For this assignment, I chose to explore the library called *Pandas*.
This markdown file discusses this library.
By the end of this document the following questions will be answered:
- What is Pandas
    - What purpose does it serve?
    - How is it used?
- What are the functionalities?
- Why was it selected for this exploratory assignment?
- How did the learning of this library influence the learning of python?
- How was my personal experience with this library?

## What is Pandas?

### What is Pandas' purpose?
In *2008* Pandas began development, by *2009* it became open sourced. It is now maintained by a community of individuals across the world [[ref](https://pandas.pydata.org/about/index.html)].
Pandas is a python library designed for working with data sets, it is used for analyzing, cleaning, manipulating and exploring data [[ref](https://www.w3schools.com/python/pandas/pandas_intro.asp#:~:text=What%20is%20Pandas%3F,by%20Wes%20McKinney%20in%202008.)].

### How is Pandas used?
Pandas has a wide variety of abilities, this section will into detail on how it is used.

Pandas' strength comes from it's ability to work with data. Many of these strengths would not be possible without DataFrames. A DataFrame is a 2-dimensional labeled data structure with columns of potentially varying types. It can be thought of as a spreadsheet or an SQL table. A 1-dimensional DataFrame is called a series [[ref](https://pandas.pydata.org/docs/user_guide/dsintro.html#)]. 


<p align="center"><img width="500" alt="" src=https://pynative.com/wp-content/uploads/2021/02/dataframe.png></p>
<p align="center"> Example of a DataFrame </p>


Much can be done using DataFrames, to name a few examples:
- <u>Data cleansing</u>
    - Fix or remove unwanted/corrupted data.
- <u>Data fill</u>
   - Fill in missing data.
- <u>Data normalization</u>
    - Reorganization of data for visualization/manipulation simplicity.
- <u>Data visualization</u>
    - DataFrames can easily be printed and/or written to a file for easy and clean visualization.
- <u>Data manipulation, inspection and analysis</u>
    - A variety of operations are available to the programmer for data manipulation. Some of these operations are:
        - Insert/remove rows or columns
        - Column renaming
        - Edit values held in the DataFrame
        - Creating subsets of data
        - Sorting
        - Grouping
        - Getting key values based on data (min, max, mean, median etc.)
        - etc.
[[ref](https://www.activestate.com/resources/quick-reads/what-is-pandas-in-python-everything-you-need-to-know/)]


Pandas can read and write data from various formats, such as
- CSV
- EXCEL
- Text Files
- SQL Databases
- etc.
[[ref](https://pandas.pydata.org/about/index.html)]

The beauty of Pandas lies in it's ease of use. Many seemingly complex operations can be done in a simple manor. See the following section for examples of Pandas functionality. 

## Functionality
Pandas has many functionalities, this section will provide sample code and outputs.


### Importing Pandas
To use Pandas, the library must be imported as such:
```python
import pandas as pd
```

### Creating a DataFrame
Creating a DataFrame;
```python
#Initialize the data values
dataValues = {
  #column name: [row values separated by commas], ...
  "column1": [1, 2, 3],
  "column2": [4, 5, 6]
}

#Convert the data values into a DataFrame
dataFrame = pd.DataFrame(dataValues)
```
The DataFrame would be displayed as: 

<p align="center"><img width="200" alt="Screenshot 2024-02-12 at 3 39 17 PM" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-calebcarr77/assets/97684864/30ae2ed1-41f9-4251-b806-8a1ce8acfbb4"></p>


### Inserting and removing columns
Using the DataFrame created above:

There are a variety of ways to insert a column into a DataFrame, the following will describe column insertion using the .insert() method. 
```python
dataFrame.insert(2, "column3", [7, 8, 9], True)
```
The DataFrame would now be displayed as:

<p align="center"><img width="300" alt="Screenshot 2024-02-12 at 4 12 58 PM" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-calebcarr77/assets/97684864/8aac2cca-21f8-406e-9c56-29b899d114db"></p>



To remove a column there is a function .drop(). This method takes in a variety of parameters, allowing columns to be dropped in many different ways. One example of how to drop a column is as follows:
```python
#The parameters correpsond to 1) the column index and 
#2) the axis parameter dictates whether the column will 
#be selected by index or name
dataFrame = dataFrame.drop(dataFrame.columns[[0]], axis=1)
```
The DataFrame would now be displayed as:

<p align="center"><img width="200" alt="Screenshot 2024-02-12 at 4 14 20 PM" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-calebcarr77/assets/97684864/48a7c11d-7106-4255-acb8-342c25e5f4ca"></p>



### Reading data from CSV or Excel File and converting to a DataFrame
To read in data from a CSV file and convert it to a DataFrame:
```python
#where 'dir' is the full directory path of the CSV file
data = pd.read_csv(dir)
dataFrame = pd.DataFrame(data)
```
To read in data from a Excel file and convert it to a DataFrame:
```python
#where 'dir' is the full directory path of the excel file
data = pd.read_excel(dir)
dataFrame = pd.DataFrame(data)
```
### Writing to a CSV or Excel File
Writing a DataFrame to CSV file can be done in one line of code as shown:
```python
#String inside of parathesis is the name of the file to 
#be written to
df.to_csv('data.csv')
```
Similarily, writing a DataFrame to an Excel file can be done in one line of code as shown:
```python
#String inside of parathesis is the name of the file 
#to be written to
df.to_excel('data.xlsx')
```
### Creating a subset of a DataFrame

To create a subset based on a DataFrame, the following code can be used:
```python
#Can include any amount of columns by separating 
#their names with commas
subDataFrame = dataFrame[["column2"]]
```
The subset DataFrame would display as:

<p align="center"><img width="175" alt="Screenshot 2024-02-12 at 4 24 19 PM" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-calebcarr77/assets/97684864/83592cf9-104c-4821-9690-34c170956f5f"></p>


Pandas is a powerful tool with a massive amount of functionalities. Pandas' [official documentation](https://pandas.pydata.org/docs/) outlines the full capabilities.  



## Why was Pandas chosen for this activity
I chose to explore Pandas as I saw it's value in data manipulation/analysis. My roommate and close friend is a chemical engineering student. Often, he is working with Excel sheets, performing data analysis and/or manipulation. I saw that writing a program to ease his data manipulation/analysis responsabilities could be of great use to him. Upon researching for this activity, using Pandas became a clear decision as it is an extremely well documented and powerful tool.

## How did learning Pandas influence my learning of the language?
Learning Pandas was a great opportunity to improve my Python skills. I feel I am completing this activity a better, more curious and eager programmer. I wrote this program using Jupyter Notebook, which I had no prior experience with, that was also a great learning opportunity.

## My overall experience with Pandas
My experience with Pandas was great. It is an easy to pick up, powerful tool. I would recommmend Pandas to anyone working with data. Understanding Pandas will be a great asset throughout my programming career, especially if I am working with data suitable for Pandas' capabilities. I will absolutely continue to use it.
