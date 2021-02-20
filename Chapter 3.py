#random import
import random
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1
total = die1 + die2
print("You rolled a", die1, "and a", die2, "for a total of", total)
#randint(x,y) function makes a random number from the range of x to y so for exmample if randint(1,6) it will produce a random number from 1 - 6
#randrage(x) will produce a random number from the range of the number including zero. so if it is randrange(6) the list of possible numbers would be from 0-5
#branching is a fundamental part of programming.
print("\n\n\n\n\n")
#if statement
print("Welcome to System Security Inc.")
print("-- where security is our middle name\n")
print("\n for demonstration purposes the password is \"secret\"\n")
password = input("Enter your password: ")
if password == "secret":
    print("\nAccess Granted")
else:
    print("\n ACCESS DENIED. CALLED POLICE. COMING IN 5 MINUTES")
#All if statements have a condition. A condition is just an expression that is either true or false.
#True = true False = false, if in the program we made the user placed "secret" it would be true, anything else would be false.
#== equal to != not equal to > < >= <=
#indentation in Python is very important. ONe exmaple of using indentation is the if statement.
#Else means if the if statement is false this executes.
#elif can contain a sequence of conditions basically like the if and else statements
print("\n\n\n\n\n\n")
print("I sense your energy. Your true emotions are coming across my screen.")
print("You are...")
ready = input("\nAre you ready?")
mood = random.randint(1,3)

if mood == 1:
    print("""\n 
_________________
|               |
|   O       O   |
|       <       |
|   .       .   |
|    .......    |
L_______________|
""")
    print("\nYou are happy!")

if mood == 2:

    print("""\n 
_________________
|               |
|   O       O   |
|       <       |
|    .......    |
|   .       .   |
L_______________|
""")
    print("\nYou are sad.")


elif mood == 3:
    print("""\n 
_________________
|               |
|   O       O   |
|       <       |
|               |
|    .......    |
L_______________|
""")
    print("\nYou are neautral.")



