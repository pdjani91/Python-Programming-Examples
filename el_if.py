age = int(input("Enter your Age : "))

if age == 0:
    print("You can't watch")

elif 0 < age <=3:
    print("Tickit Price : FREE")
elif 3 < age <=10:
    print("Tickit Price : 150")
elif 10 < age <=60:
    print("Tickit Price : 250")
else: 
    print("Tickit Price : 200")