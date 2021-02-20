#for loop
word = input("Enter a word: ")

print("\nHere's each letter in your word: ")
for letter in word:
    print(letter)

#range("x,y,multiplier"
print("\n\n\n\n\n")
for i in range(0,50,5):
    print(i, end=" ")


message = input("\n\n\n\n\n\nEnter a message: ")
print("\n The length of your message is:", len(message))
print("\n The most common letter in the English Language, 'e'")
if "e" in message:
    print("is in your message")
else:
    print("is not in your message ")

