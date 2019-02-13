winning_number = 43
guess = 1
number = int(input("Enter number between 1 to 100 : "))
game_over = False

while not game_over:
    if number == winning_number:
        print(f"You win, and you guessed this number in {guess} times")
        game_over = True
    else:
        if number < winning_number:
            print("Too Low")
            guess += 1
            number = int(input("Guess again : "))
            
        else:
            print("Too High")
            guess += 1
            number = int(input("Guess again : "))
            
            