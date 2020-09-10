'''
                            TASK TWO: OPERATORS AND DECISION MAKING STATEMENT
1.	Write a program in Python to perform the following operation:
●	If a number is divisible by 3 it should print “Consultadd” as a string
●	If a number is divisible by 5 it should print “c” as a string
●	If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.
'''
###
# a = float(input("Enter desired number: "))

#while (a%3==0):
#    print("Consultadd")
#else:
#    print("number is not divisible by 3") 
###

b = float(input("Enter desired number: "))

if (b%3==0 and b%5==0):
    print("Consultadd Python Training")
elif b%3==0:
    print("“Consultadd”")
elif b%5==0:
    print("c")
else:
    print("Number not divisible by 3 or 5")


