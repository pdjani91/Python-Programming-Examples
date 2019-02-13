#Ask user to input 3 numbers and you have to print avarage of three numbers using string formatting.
a,b,c=input("Enter Three Numbers using Comma Sepearated :").split(",")

print(f"Averege is {(int(a)+int(b)+int(c)/3)}")