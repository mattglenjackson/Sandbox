password = input("Enter Password: ")
while len(password) < 6:
    print("Password needs to be more than 5 characters")
    password = input("Enter Password: ")

for i in range(len(password)):
    print("*", end="")