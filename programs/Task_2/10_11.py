'''
10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
           		counter=1
		While counter <= 5:
			print(“Type in the”, counter, “number”
			counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.
'''
number = 0
answer = 22
c=1
while (c <=5):
    
    if (number == answer and c<=5):
        print("Good guess!")
else:
    number = int(input("guess the lucky number : "))
    c+=1
