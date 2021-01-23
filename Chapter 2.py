#Chapter 2 Types Variables and Simple I/O: The useless trivia program
print("THIS IS PRINTED 10 TIMES!\n" * 10)
#\n NEW LINE
#\# special characters
#\t Moves cursor Forward one tab stop
#'+' can connect lines
#* can multiply
#+-*/ what they do, // Integer, %modulous
#upper() : uppercase, lower() : lowercase, swapcase() : Swaps capitalized to lower case and vice versa,
#capitalize() : capitalized every letter, title() : first letter capitalized, strip() : removes all white space,
#replace(old, new [,max]): old -> new | max : max amount of replacements

print("\n\n\n\n\n\n\n\n\n\n\n\n")
print("WELCOME TO THE USELESS TRIVIA BOT!")
print(" ")
name = input("Hi. What's your name?")
print("Hi " + name)
age = int(input("How old are you? "))
weight = int(input("Okay, last question. How many pounds do you weigh?"))

print("\nIf your mom is calling you she would address you as " + name.lower())
print("But if your mom was mad she would address you as " + name.upper())

print("\nIf a little child was trying to get your attention your name would become")
print(name.title() * 5)

print("\nYou're over", str(age * 365 * 24 * 60 * 60), "seconds old.")

print("\n Did you know that on the moon you would weigh only", str(weight / 27.1), "pounds?")

print("\n On the sun, you'd weigh", str(age * 27.1), "(but, ah... not for long)." )

print("\n Thank you for using the Useless Trivia bot! Come back with a friend!")


