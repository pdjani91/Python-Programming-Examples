def greter(a,b,c): # a and b is parameter
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
num3 = int(input("Enter 2nd Number : "))

bigger = greter(num1,num2,num3)

print(f"{bigger} is greatest")