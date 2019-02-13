def greter(a,b): # a and b is parameter
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
bigger = greter(num1,num2)

print(f"{bigger} is greater")
