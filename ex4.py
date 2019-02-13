winning_number = 24

guess_number = int(input("Enter your guessing number :"))

if guess_number == winning_number:
    print("WIN")
else:
    if guess_number < winning_number:
        print("Too Low")
    else:
        print("Too High")