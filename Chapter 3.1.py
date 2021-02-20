#Matthew Simulator
print("\tWelcome to the'Matthew Simulator'")
print("\nThis program simulates a conversation with Matthew.")
print("\nTry to stop him.")
print(" ")
response = ""
while response != "Because.":
    response = input("Why?\n")

print("Ahhhhh... Okayyy.. I'll research first.")

#Losing Battle
#Demonstrates the Dreaded infinite loop
print("\n\n\n\n\n\n")
print("Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out. Melting into the horizon.")
print("Your hero unsheathes his sword for the last fight of his life")
health = 10
trolls = 0
damage = 3

while health > 0:
    trolls += 1
    health -= damage

    print("Your hero swings and defeats an evil troll,  ", "but takes", damage, "damge points.\n")

print("Your hero fought valiantly and defeated", trolls, "trolls.")
print("But alas, your hero is no more.")
