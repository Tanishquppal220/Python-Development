n = 76
print("Guess the Number Game")
print("Total Guess = 5")
guess = 5
game_over = False

while guess<=5:
    i = int(input("Enter a number:\n"))
    if i<n: 
        print("Higher")
        if guess==1:
            print("Game Over")
            break
        else:
            guess -= 1
        print("Guess Left:",guess)
    elif i>n:
        print("Lower")
        if guess == 1:
            print("Game Over")
            break
        else:
            guess -= 1
        print("Guess Left:", guess)
    elif i==n:
        print("Correct")
        break

