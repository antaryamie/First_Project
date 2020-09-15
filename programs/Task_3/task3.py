'''
1.	Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.
2. 	Create a list of size 5 and execute the slicing structure 
3.          Write  a program to get the sum and multiply of all the items in a given list.
4.   	Find the largest and smallest number from a given list.
5. 	Create a new list which contains the specified numbers after removing the even numbers from a predefined list. 
'''

# 1
'''
x = list1 = [0,1,771524171903, "apple", "mango", 4j, dict(name='Harsh', age='24'), (101, "Peter", 22), {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}, set(["home","office"])]
print(x)
print(len(x))
'''

# 2
'''
# l = [1] * 5


l = []
l.insert(0,1)
l.insert(1,2)
l.insert(2,3)
l.insert(3,4)
l.append(5)
print(len(l))
print(l)

print(l[0])  
print(l[1])  
print(l[2])  
print(l[3])  
# Slicing the elements  
print(l[0:5])  
# By default the index value is 0 so its starts from the 0th element and go for index -1.  
print(l[:])  
print(l[2:5])  
print(l[1:5:2])  

'''

# 3

# Sum
'''
l = [1,2,3,4,5,99]
sum = 0

for i in range(0, len(l)):
    sum = sum + l[i]
    
print(sum)
'''
# Multiplication
'''
l = [1,2,3, 4]

Multiplication = 1

for i in range(0, len(l)):
    Multiplication = Multiplication * l[i]
    
print(Multiplication)
'''

# 4

'''

l = [401,243,452,123,420,312]

l.sort()

print(l)
print("smallest number" , l[0])

##########################


l = [401,243,452,123,420,312]

l.sort()

print(l)
print("largest number" , l[-1])


'''


# 5
'''
a = [4, 32, 11, 342, 333, 532, 112, 443, 567]
b = [i for i in a if i%2!=0]

print(b)
'''

'''
6.	Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
7.	Write a program to replace the last element in a list with another list.
Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
Expected output: [1,3,5,7,9,2,4,6,8]
8.	Create a new dictionary by concatenating the following two dictionaries:
a={1:10,2:20}
b={3:30,4:40}
Expected Result: {1:10,2:20,3:30,4:40}
9.	Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
Sample data (n=5)
Expected Output: {1:1,2:4,3:9,4:16,5:25}
10. 	Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program:
34,67,55,33,12,98
The output should be:
[‘34’,’67’,’55’,’33’,’12’,’98’]
(‘34’,’67’,’55’,’33’,’12’,’98’)
'''

# 6

'''

def funPrintVal():
	l = list()
	for i in range(1,31):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

funPrintVal()
'''


# 7

'''
l1 = [1, 3, 5, 7, 9, 10]
l2 = [2, 4, 6, 8]
l1[-1:] = l2
print(l1)
'''


#8
'''

a={1:10,2:20}
b={3:30,4:40}

def Merge(a, b):
    return(a.update(b))

Merge(a,b)

print(a)

'''

# 9
'''
n = 5
d = dict()

for i in range(1,n+1):
    d[i]=i*i

print(d) 
'''

# 10

'''
values = input("Please input a few comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
'''