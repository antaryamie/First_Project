'''
2. 	Write a program in Python to perform the following operator based task:
    • Ask user to choose the following option first:
        ◦ If User Enter 1 - Addition 
        ◦ If User Enter 2 - Subtraction
        ◦ If User Enter 3 - Division
        ◦ If USer Enter 4 - Multiplication
        ◦ If User Enter 5 - Average
    • Ask user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
    • Ask user to enter two more numbers as first and second2 for calculating the average as soon as user choose an option 5.
    • At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
    • NOTE: At a time user can perform one action at a time.
'''

c = float(input("enter first number: "))
d = float(input("enter second number: "))
r = float
print('''Enter 1 for Addition
Enter 2 for Subtraction
Enter 3 for Division
Enter 4 for Multiplication
Enter 5 for Average : ''')
s = int(input("Choice: "))

while s<6:
    if s==1:
        r=c+d
        print("Addition: ", r)
        if r < 0:
            print("NEGATIVE")
        break
    if s==2:
        r=c-d
        print("Subtraction: ", r)
        if r < 0:
            print("NEGATIVE")
        break
    if s==3:
        r=c/d
        print("Division: ", r)
        if r < 0:
            print("NEGATIVE")
        break
    if s==4:
        r=c*d
        print("Multiplication: ", r)
        if r < 0:
            print("NEGATIVE")
        break
    if s==5:
        e = float(input("enter third number: "))
        f = float(input("enter fourth number: "))
        r=(c+d+e+f)/4
        print("Average: ", r)
        if r < 0:
            print("NEGATIVE")
        break
else:
    print("please enter a valid choice")
    
