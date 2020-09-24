'''
TASK FIVE: FILE HANDLING AND EXCEPTION HANDLING
1.	Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError
2. 	Write a program in Python to allow user to open a file by using argv module. If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode. 
3. 	Write a program to handle an error if the user entered the number more than four digits it should return “Please length is too short/long !!! Please provide only four digits” 
4. 	Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.
5. 	https://www.programiz.com/python-programming/exception-handling Go through this link to understand Finally and Raise concept.
6. 	Read any file using Python File handling concept and return only the even length string from the doc.txt file.
Consider the content as: 
	Hello I am a file 
	Where you need to return the data string 
	Which is of even length 
	Make sure you return the content in 
	The same link as it is present.

'''
# 1.

try:
    eval('6=7')
except SyntaxError:
    print("Error in Syntax")

# 2.

## need to supply agruments when running the file.

import sys
def checkFile(filename):
    try:
        with open(filename, 'r') as file:
            print("File Opened")
            file.close
            print("File Closed")
    except FileNotFoundError:
        filename = input("No such file exists.\nEnter filename again: ")
        checkFile(filename)

checkFile(sys.argv[1])

# 3.

def checkDigits(num):
    if not '.' in num:
        return len(num)
    return len(num[:num.index('.')])

var1 = input("Enter a number: ")

if checkDigits(var1) != 4:
    print("Please length is too short/long !!! Please provide only four digits.") 

# 4.

count = 0
while(True):
    try:
        username = input("Username: ")
        password = input("Password: ")
        repass = input("Re-Type Password: ")
        if password != repass:
            raise Exception
        else:
            break
    except:
        if count < 3:
            count+= 1
        else:
            print("Maximum Attempts Reached.")
            break

# 6.

try:
    with open("sample.txt", 'r') as file:
        for line in file:
            if len(line) % 2 == 0:
                print(line)
        file.close
except:
    print("File Error")