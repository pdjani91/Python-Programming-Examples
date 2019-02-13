name = input("Enter your name : ")
age = int(input("Enter your age : "))

if age >= 10 and (name[0]=='a' or name[0]=='A'):
    print("You can watch this movie")
else:
    print("You can't watch this movie")