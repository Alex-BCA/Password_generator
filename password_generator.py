import random
print("***Password generator***")
while True:
    print("1.Generate password")
    print("2.Exit")

    choice=input("Enter your choice:")
    if choice=="1":
        print("Create password:")
        length=int(input("Enter password length:"))
        chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        password=""
        for i in range(length):
            password+=random.choice(chars)
        print("Generated password =",password)
    elif choice=="2":
        print("Thank you!")
        break
    else:
        print("In-valid choice")
