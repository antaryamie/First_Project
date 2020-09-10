'''
8.  Write a program that accepts a string as an input from user and calculate the number of digits and letters.
     Expected output: consul12
     Letters 6
     Digits 2
'''

s = "consul12"
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print(s)
print("Letters", l)
print("Digits", d)