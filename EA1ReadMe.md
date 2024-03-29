# Pandas
This program provides a demonstration of the library *Pandas*.

# How to run this program
This program can be run in different ways based on the IDE used. In Jupyter Notebook, it can be ran using Shift+Return on the cell containing the main loop. If downloaded onto another IDE it can be run using the terminal.

# Purpose of program
This purpose of this program is to demonstrate basic functionality of Pandas. These functions are:
- read data from CSV or Excel file
- shape
- sum
- min
- max
- add column
- view data
- write data to file

# Program restraints
This program has a few restraints. Mainly, it is designed entirely around data that holds only integers. In practice Pandas and DataFrames can make use of a variety of types.

# Examples of I/O
Upon running the program, the user is prompted to decide if they would like to read in either a CSV or Excel file for manipulation/analysis. Once they have decided the file type and entered the directory path of their file, a function is called that asks them what operation they would like to perform. The user can type 'exit' at any time to terminate the program.
Below is examples of some of these functions at use, *blue highlights are input, purple highlights are outputs.*

The CSV file in the examples of I/O is shown in the screenshot below:
<p align="center"><img width="200" alt="Screenshot 2024-02-12 at 9 49 38 PM" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-calebcarr77/assets/97684864/6d303be2-2961-414d-a4b2-b4dcdaa6ae61"></p>

### Getting the program started and using *shape*

The screenshot below shows the beginning phase of the program. The user is prompted to enter the file type and path, then given an option of operations to be done on the data. In this case the user selected shape, this prints the number of rows and columns 
<p align="center"><img width="965" alt="Screenshot 2024-02-12 at 9 43 42 PM" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-calebcarr77/assets/97684864/13c40f1c-c44f-4cb2-8ad2-1c8c60597d1f"></p>


### Using *sum*
Below shows the use of the sum operation, this takes the sum of the values in the columns. In this program the user has the ability to decide if they want to get the sum of specific columns or all columns.

<p align="center"><img width="960" alt="Screenshot 2024-02-12 at 10 26 56 PM" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-calebcarr77/assets/97684864/1627ae3f-b88a-4b1a-91ee-8c4ed81ad2e7"></p>


### Using *min*
Min and max are both used in the exact same way. Upon selecting the operation, the user selects the columns of which they would like inspected, then the result is printed. See an example of min below.
<p align="center"><img width="968" alt="Screenshot 2024-02-12 at 10 46 29 PM" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-calebcarr77/assets/97684864/e9e70b98-ef14-4a6f-b23a-2d5082592804"></p>


### Using *add* and *view*
The add operation allows the user to add another column to the DataFrame. Once the user has selected the add operation, they are prompted to choose the column index, column name, and column value. There are measures implemented to make sure the index and column values to not end up being out of range of the DataFrame in question. View is a simple operation, it simply displays the DataFrame. See example below:

<p align="center"><img width="1235" alt="Screenshot 2024-02-12 at 11 24 48 PM" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-calebcarr77/assets/97684864/36c8c4b0-ba22-431f-84de-79a599185272"></p>


### Using *write*
Write is simply done by asking the user what type of file they would like to write to and what they would like to name the file. See screenshots below to view the writing process as well as the resultant file.
<p align="center"><img width="1286" alt="Screenshot 2024-02-12 at 11 14 16 PM" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-calebcarr77/assets/97684864/07042b66-2927-42e3-8bdc-0f11721568ee"></p>
<p align="center"><img width="250" alt="Screenshot 2024-02-12 at 11 14 55 PM" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-calebcarr77/assets/97684864/89e8544a-e113-4b77-aaad-b59ebac3f95c"></p>

