#Word Jumble
import random
WORDS = ("burger","fries","Matthew","potato","nice","truck")
word = random.choice(WORDS)
jumble =""
correct = word
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
b
print("""
              Welcome to Word Jumble
        Unscramble the letters to make a word
        
""")

print("\nThe jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess:")

if guess == correct:
    print("That's it! You guessed it!\n")
