'''
TASK ONE: NUMBERS AND VARIABLES

1.	Create three variables in a single line and assign different values to them and make sure their data types are invited differently. Like one is int, another one is float and last one is string.
a = 1; b = 2.01; c = 'string'
'''

a, b, c = 1, 2.01, 'python'
print(type(a), type(b), type(c))
print(a,b,c)

'''
2. 	Create a variable of value type complex and swap it with another variable whose value is an integer.
'''

complexnum = 1+3j
print(type(complexnum))

num1 = int(20)
print(type(num1))

complexnum, num1 = num1, complexnum
print(complexnum, num1)

var1 = "hp"
var2 = "Dp" 
var3 = "swap"

print(var1,var2, var3)

var1, var3 = var3, var1
print(var1, var3)

var1, var2 = var2, var3
print(var1, var2)


'''
4. 	Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.
'''

'''
python2.x

x = raw_input("Enter you name : ")
print(x)

'''

'''
python 3.x

y = input("provide any input: ")
print(y)

z = int(input("Enter integer: "))
print(z)

'''

'''
5. 	Write a program to complete the task given below:
●	Ask user to enter any 2 numbers in between 1-10 and add both of them to another variable  call z.
●	Use z for adding 30 into it and print the final result by using variable result.


usernum1 = int(input("enter number1 between 1 to 10: "))
usernum2 = int(input("enter number2 between 1 to 10: "))
print(usernum1, usernum2)
z = usernum1 + usernum2
print("total: ", z)

z+=30

print(z)

'''

'''
6. 	Write a program to check the data type of the entered values. 
HINT: Printed output should say -  The input value data type is : int/float/string/etc
'''

q = 20j
print("The input value data type is : ", type(q))
w = 20.1
print("The input value data type is : ", type(w))
e = "antaryamie"
print("The input value data type is : ", type(e))
r = 20
print("The input value data type is : ", type(r))
t = [1.2,3]
print("The input value data type is : ", type(t))
y = True
print("The input value data type is : ", type(y))
u = '''multi
        line
        string'''
print(u, type(u))
i = ("hi", "python", 2, 3j, 30.2)
print("The input value data type is : ", type(i))
o = {1 : 'hi',
     2 : 2 ,
     3 : '20.2'}

print("The input value data type is : ", type(o))

set1 = {1,2,"python",20.2, 4j}
print("The input value data type is : ", type(set1))

'''
7. 	Create Variable using CamelCase, LadderCase and UPPERCASE. (Refer:   https://capitalizemytitle.com/camel-case/)
'''

# Camel Case
nameOfStudent, valueOfVaraible = "Antaryamie", 20
# Pascal Case 
NameOfStudent, ValueOfVaraible = "Antaryamie", 20
# Snake Case
name_of_student, value_of_variable = "Antaryamie", 20
# UPPERCASE
NAME_OF_STUDENT = "Antaryamie"

'''
8. 	If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value. If Yes then Why?
'''

a = int(20)
print("type of a: ", type(a))

a = 20j
print("type of a: ", type(a))

'''
Ans. Python is dynamically typed so yes If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. It will change the value.
'''

