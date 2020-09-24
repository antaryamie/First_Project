'''
TASK SIX: HIGHER ORDER FUNCTIONS, GENERATORS, LIST COMPREHENSION AND DECORATOR
1.	Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. Make sure to use only higher order function.
2. 	Write a program in Python to  multiple the element of list by itself using traditional function and pass the function to map to complete the operation.
3. 	Write a program to Python find out the character in a string which is uppercase using list comprehension.
4. 	Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should maps the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension. HINT-Use Zip function also
Student = ['Smit', 'Jaya', 'Rayyan']	
capital = ['CSE', 'Networking', 'Operating System']
5. 	Learn More about Yield, next and Generators
6. 	Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”
7. 	Write any example on decorators.
8. 	Learn about What is FRONT END and its Technologies and Tools
Make sure to mention at least 5 top notch technologies of Frontend.
Also mentioned the name of companies using those 5 technologies individually
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