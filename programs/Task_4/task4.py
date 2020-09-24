'''
TASK FOUR: FUNCTIONS
1. 	Write a program to reverse a string.
Sample data: “1234abcd”
Expected Output: “dcba4321”
2. 	Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
Expected Output:
No. of Upper case characters : 3
No. of Lower case Characters : 12
3.        Create a function that takes a list and returns a new list with unique elements of the first list.
4.         Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
'''
# 1

# def reverse_string(str):
#     user_input = input("Enter desired string: ")
#     result = print('reverse sting is : ', user_input[::-1])

#     return result

# x = str
# reverse_string(x)

# 2 
# def count(str):
#     x = input('Enter string: ')
#     uppercase_char = 0
#     lowercase_char = 0
#     for i in str(x):
        
#         x = i.split(" ")
#         if i.isupper() == True:
#             uppercase_char += 1
#             print('number of uppercase',uppercase_char)
#         else:
#             lowercase_char += 1
#             print('number of lowercase', lowercase_char)

# y = str
# count(y)

# Require Assistance


# 3

# def unique_list(l):
#   x = []
#   for a in l:
#     if a not in x:
#       x.append(a)
#   return x

# print(unique_list([1,2,2,2,3,3,3,3,4,5,6,66,7,888,8,8,8,8,88,8])) 



# 4

# def function1(str):
#     str = input('Enter hyphern seperated string: ' )
#     str.split('-')
#     str.sort()
#     print('-'.join(str))
#     return str
# x=str
# function1(x)


# Require Assitance



'''
5.         Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Sample input:
Hello world
Practice makes perfect
Expected Output:
HELLO WORLD
PRACTICE MAKES PERFECT
'''


# def capitalize(str):
#     lines = []
#     while True:
#         s = input()
#         if s:
#             lines.append(s.upper())
#         else:
#             break
#     for sentense in lines:
#         print(sentense)
    
# x = str
# capitalize(x)

'''
6.          Define a function that can receive two integral numbers in string form and compute their sum and print it in console.

'''

# def sum(int1, int2):
#     int1 = int(input("enter first number  "))
#     int2 = int(input("enter first number  ")) 
#     s = int1 + int2
#     return print(s)

# sum(2,3)

    

'''
7.        Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
'''

# def one(in1, in2):
#     in1 = str(input('Enter 1st str:   '))
#     in2 = str(input('Enter 2nd str:   '))

#     if len(in1) > len(in2):
#         print(in1)
#     elif len(in2) > len(in1):
#         print(in2)
#     elif len(in1) == len(in2):
#         print(in1)
#         print(in2)
#     else:
#         print('valid strings  ')
# x, y = str, str       
        
# one(x, y)

'''
8.        Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.
'''

def two():
    t = tuple()
    for i in range(1,21):
        t.add(i**2)
        
    print(t)
    
two()

    
    


'''
9.         Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
Example: If the limit is 3 , it should print:
0 EVEN
1 ODD
2 EVEN
3 ODD
10. 	Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)
11. 	Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
Hints: Use map() to generate a list.
     	     Use filter() to filter elements of a list
            Use lambda to define anonymous functions
12. 	Write a function to compute 5/0 and use try/except to catch the exceptions
13. 	Flatten the list [[1,2,3],[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
Goal : Turn [1,2,3,4,5,6,7] to 1234567 

 14. 	What is the output of the following codes:
(i) def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

(ii) def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')
a()
'''


# 8.

def generateSquares(i):
    return (i*i,)
result3 = generateSquares(5)

# 9.

def showNumbers(limit):
    for i in range(limit+1):
        print("{} EVEN".format(i)) if i%2==0 else print("{} ODD".format(i))

showNumbers(5)

# 10.

remove_even = lambda x:x%2==0
result4 = list(filter(remove_even, list(range(1,21))))

# 11.

var2 = [1,2,3,4,5,6,7,8,9,10]
result5 = [*map(lambda x:x*x, filter(remove_even, var2))]

# 12.

try:
    var3 = 5/0
except BaseException as e:
    print("Cannot Divide", e)

# 13.

from functools import reduce
var4 = [[1,2,3],[4,5],[6,7,8]]
result6 = reduce(lambda x,y:x+y, var4)
# result6 = reduce(lambda x,y:str(x)+""+str(y), var4)


# 14.

# return 2
# error
