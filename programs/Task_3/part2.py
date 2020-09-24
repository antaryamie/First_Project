'''
MORE QUESTIONS ON DATA STRUCTURES

3. 	Create a list of given structure and run 
	x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
Access list [1, 2, 3, 4]
Access list [600,  700]
Access list [100, 300, 500, 600, 800]
Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
Access list [10]
Access list [ ]
4. 	Create a list of thousand number using range and xrange and see the difference between each other.
5. 	How Tuple is beneficial as compare to the list?
6. 	Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and a multiple of 2.
7. 	Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with their index.
8. 	Write a program in Python to iterate through the string “hello my name is abcde” and print the string which has even length of word.
9. 	Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.
x=[1,2,3,4,5,6,7,8,9,-1]

'''


# 3
'''
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][:4])
print(x[-3:-1])
print(x[::2])
print(x[::-1])
print(x[5][5][0])
print(x)
'''

#4

# In python3 .range() will be implemented by the Python 2 .xrange(). 
'''
Difference between Python xrange and range
The two range functions have many different traits. These could relate to performance, memory consumption, speed, and internal design. Each of these has its implementation differently. Now, let’s review each such differences one by one.

Operational difference
In most cases, both xrange and range operate precisely in the same way. They both give a way to produce a list of numbers for you to use.

Hence, we can say that both are similar in terms of functionality. Let’s see some examples now:

The expression range (1, 7, 2) will produce [1, 3, 5] and xrange(1, 7, 2) will produce [1, 3, 5]. Hence, you can conclude that they have a similar execution pattern and output.

Return values and type
It is the primary source of difference between Python xrange and range functions.

The range() returns a list type object. For example, the expression range(1, 100, 1) will produce a 99 int numbers range. It gets all the numbers in one go.

>>> r = range(1, 100, 1)
>>> type(r)
<type 'list'>
>>> len(r)
99
On the other hand, the xrange() provides results as an xrange object. It performs a lazy evaluation. It keeps the arguments and produces numbers on call. Unlike range(), it avoids getting all the number in one go.

The xrange object allows iteration, indexing, and the len() method. You can have a for loop to traverse it and gets the numbers in every iteration.

>>> xr = xrange(1, 100, 1)
>>> type(xr)
<type 'xrange'>
>>> xr[0]
1
>>> for it in xr:
...    print(it)
...
1
2
3
...
99
'''

#5
'''
Different Use Cases
At first sight, it might seem that lists can always replace tuples. But tuples are extremely useful data structures

Using a tuple instead of a list can give the programmer and the interpreter a hint that the data should not be changed.
 
Tuples are commonly used as the equivalent of a dictionary without keys to store data. For Example,
[('Swordfish', 'Dominic Sena', 2001), ('Snowden', ' Oliver Stone', 2016), ('Taxi Driver', 'Martin Scorsese', 1976)]
Above example contains tuples inside list which has a list of movies.
 
Reading data is simpler when tuples are stored inside a list. For example,
[(2,4), (5,7), (3,8), (5,9)]
is easier to read than
[[2,4], [5,7], [3,8], [5,9]]
Tuple can also be used as key in dictionary due to their hashable and immutable nature whereas Lists are not used as key in a dictionary because list can’t handle __hash__() and have mutable nature.

key_val= {('alpha','bravo'):123} #Valid
key_val = {['alpha','bravo']:123} #Invalid
Key points to remember:
The literal syntax of tuples is shown by parentheses () whereas the literal syntax of lists is shown by square brackets [] .
Lists has variable length, tuple has fixed length.
List has mutable nature, tuple has immutable nature.
List has more functionality than the tuple.

'''

# 6

'''
for i in range(0, 1101, 3): 
    print("divisible by 3", (i))

for i in range(0, 1101, 5): 
    print("divisible by 5", (i))
'''

# 7

'''
x = "abcdefgh"

print(x[::-1])

def removeVowels(word:str):
    if(i=a, e, i, o, u, A, E, I, O, U):
    
    Require assistance
'''

# 8   
'''
def even_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 != 0:
      result = result + str[i]
  return result

print(even_values_string('hello my name is abcde'))
Require assistance
'''

# 9

# Require assistance
'''
10. 	Write a program in Python to complete the following task:
Create two different list as in even_list and odd_list
Ask user to enter the number in the range of 1,50 and make sure if the entered number is even append it to the even_list and if the entered number is odd append it to the odd list.
Keep that in mind you can only add 5 items in each list
Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list.
11. 	Write a program to find out the occurrence of a specific word from an alphanumeric statement. Example: 12abcbacbaba344ab  
                      Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic

12. Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
'''
# 10
'''
even_list = []
odd_list = []
user_input = int(input("Enter number in range of 1 to 50 : "))
l = (0,5)

for i in l:
    if i <= 5 and user_input %2 == 0:
        even_list.append(user_input)
        i+=1
        
    if i <= 5 and user_input %2 != 0:
        odd_list.append(user_input)
        i+=1
    
print(even_list)
print(odd_list)
Require assistance
'''

# 11

'''
def occuranceWord (str, word):
    
    a = str.split(" ")
    
    count = 0
    
    for i in range(0, len(a)):
        if word == a[i]:
            count+=1
        
    return count

str = "My name is abc"
word = "abc"

print(occuranceWord(str, word))
'''


# 12
'''
tuple1 = (1,2,3,4,5,6,7,8,9,10)
tuple2 = tuple(i for i in tuple1 if i%2 == 0)
print(tuple2)

'''