#Maitre D'
#demonstrates treating a value as a condition

print("Welcome to the Chateau D' Food")
print("It seems we are quite full this evening.\n")

money = int(input("How many dollars do you slip the Maitre D.?"))

if money > 0:
    print("Ah, I am reminded of a table. Right this way")
elif money < 0:
    print("I don't owe you anything! Guards! Arrest this man!")
else:
    print("Please, sit. It may be a while.")

print("\n\n\n\n\n\n")
#Finicky Counter
#Demonstrates the break and continue statements

count = 0
while True:
    count += 1
    #end loop if count greater than 10
    if count > 10:
        break
    #skip 5
    if count == 5:
        continue
    print(count)

#end loops with "break"
#contniue loops with "continue"

#Exclusive Network
#demonstrates logical operators and compound conditions
print("\n\n\n\n\n\n\n\n\n")
print("\tExclusive Computer Network")
print("\t\tMembers Only!")

security = 0

username = ""
while not username:
    username = input("Username: ")

password = ""
while not password:
    password = input("Password: ")

if username == "GBVP" and password == "secret":
    print("Hello Borge!")
    security = 5

elif username == "MTVP" and password == "burger":
    print("Hello Matt!")
    security = 3

elif username == "DHVP" and password == "sushi":
    print("Hello Dana!")
    security = 4

elif username == "GRCP" and password == "chicharon":
    print("Hello George!")
    security = 4

elif username == "guest" and password == "guest123":
    print("Welcome!")
    security = 1

else:
    print("Login failed. you're not so exclusive.\n")
