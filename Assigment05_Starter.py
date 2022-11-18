# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (VRubin,11/16/2022,Added code to complete assignment 5):
# RRoot,1.1.2030,Created started script
# VRubin,11/16/2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #
#!/bin/bash
# -- Data -- #
# declare variables and constants
objFile = None # Changed objFile to None-VLR
strFile = "ToDoList.txt"   # An object that represents a file # changed objFile to strFile-VLR
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")

for row in objFile:
    strData = row.split(",")
    dicRow = {"Task":strData[0].strip("\n")}
    lstTable.append(dicRow)
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print("\n________________________")  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print(row["Task"])

        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        while(True):
            strData = input("To do item:")
            dicRow = {"Task":strData}
            lstTable.append(dicRow)
            strChoice = input("Return to menu? ('y/n'):")
            if strChoice.lower() == 'y':
                break
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        while(True):
            strItem = input("Item to Remove:")
            for row in lstTable:
                if row["Task"] == strItem:
                    lstTable.remove(row)
                    print ("row removed")
                else:
                    print ("row not found")
            strChoice = input("Return to menu? ('y/n'):")
            if strChoice.lower() == 'y':
                break
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + "\n")
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("\n\nPress Enter to exit.")
        break  # and Exit the program
