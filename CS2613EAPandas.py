import pandas as pd

def dataOperations(df):
    flag = 0
    columnFlag = 0
    rowFlag = 0
    op = ""
    
    while(op != "exit"):
        print("What operation would you like to perfrom?")
        #get operation
        op = input("shape, sum, min, max, add collumn (type 'add'), view data (type 'view'), write data to new file (type 'write')\n")
        if op == "shape":
            #Print number of rows and columns
            print("The number of rows and columns in your data is:")
            print(df.shape)
        
        #SUM
        if op == "sum":
            columnIndex = input("Which column(s) would you like to have summed (separated by spaces)? If you would like all of them, write 'all'\n")
            if columnIndex == "all":
                print("The sum of the columns of your data is:")
                print(df.sum())
            else:
                columnIndex = columnIndex.split()
                print("The sum  of the columns inputted is:")
                print(df[columnIndex].sum())
        
        #MIN       
        if op == "min":
            columnIndex = input("Which column(s) would you like to see the minimum element of (separated by spaces)? If you would like all of them, write 'all'\n")
            if columnIndex == "all":
                print("The minimum value of each column in your data is:")
                print(df.min())
            else:
                columnIndex = columnIndex.split()
                print("The minimum values of the columns inputted is:")
                print(df[columnIndex].min())
        
        #MAX
        if op == "max":
            columnIndex = input("Which column(s) would you like to see the maximum element of (separated by spaces)? If you would like all of them, write 'all'\n")
            if columnIndex == "all":
                print("The maximum value of each column in your data is:")
                print(df.max())
            else:
                columnIndex = columnIndex.split()
                print("The maxmimum values of the columns inputted is:")
                print(df[columnIndex].max())
        
        #ADD
        if op == "add":
            columnFlag = 0
            rowFlag = 0
            #get column index
            while (columnFlag == 0):
                columnIndex = int(input("What index would you like the column to be? \n"))
                if columnIndex <= len(df.columns):
                    columnFlag = 1
                else:
                    print("Column index out of bounds, try again.")

                #get column name
                columnName = input("Enter the name of the column you would like to have added: \n")
                #get column values
                rowCount = df.shape[0]
                
                while (rowFlag == 0):
                    columnValues = input("Enter the column values (seprated by a space): \n")
                    columnValues = columnValues.split()
                    if len(columnValues) == rowCount:
                        rowFlag = 1
                    else:
                        print("Incorrect number of values, try again.")

                #convert column values to integer
                columnValues = [int(i) for i in columnValues]
                #perform insert
                df.insert(columnIndex, columnName, columnValues, True)
        
        #VIEW
        if op == "view":
            print(df)
         
        #WRITE
        if op == "write":
            flag = 0
            while (flag == 0):
                fileType = input("What type of file would you like to write your data to? CSV or Excel\n")
                fileType.lower()
                if fileType == "csv":
                    fileName = input("What would you like to name the file? Do not include file type\n")
                    df.to_csv(fileName + '.csv')
                    flag = 1
                if fileType == "excel":
                    fileName = input("What would you like to name the file? Do not include file type\n")
                    df.to_excel(fileName + '.xlsx')
                    flag = 1
                if (fileType != "csv" and fileType != "excel"):
                    print("Incorrect file type, try again.")


print("print 'exit' to exit program")
#Get file type
fileType = input("Would you like to read a CSV file or an Excel File? (Please print either CSV or Excel)\n")
fileType = fileType.lower()

#  or (dir != "exit")
while(fileType != "exit" or dir != "exit"):
    try:
    
        #Get file path and jump to function
        if fileType == "csv":
            dir = input("Please write the file path of your CSV file\n")
            data = pd.read_csv(dir)
            df = pd.DataFrame(data)
            dataOperations(df)

        #Get file path and jump to function
        if fileType == "excel":
            dir = input("Please write the file path of your Excel file\n")
            data = pd.read_excel(dir)
            df = pd.DataFrame(data)
            dataOperations(df)
        
        #If the fileType is not valid
        else:
            fileType = input("Please enter a valid file type\n")

    #If an error regarding path is thrown
    except:
        if dir == "exit":
            break
        else:
            print("File not found, try again.")
    