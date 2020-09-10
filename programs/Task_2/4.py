'''
4. 	Write a program in Python to break and continue if the following cases occurs:
    • If user enters a negative number just break the loop and print “It’s Over”
    • If user enters a positive number just continue in the loop and print “Good Going”
'''

a = int(input("enter number : "))  

while a < 0:
    
    print("It's Over")
    break

    if a >= 0:
        continue
    print("Good Going")
print("bye")

#issue with float