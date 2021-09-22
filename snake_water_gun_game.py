# Snake Water Gun game
# Snake can drink water and win.
# Gun will sink into water so water win
# Gun can kill snake so snake loose
# Process computer choice internally and 
# Ask user for their decision
# then show user loose or win or draw or invalif input
# limit user to play this game 10 times 
# And print how many times computer won and how many time user won.
import random

choicelist = ["Snake", "Water", "Gun"]
computerchoice = random.choice(choicelist)
print("Welcome to Snake Water Gun game, Good Luck!")
n = 10
w = 0
l = 0
d = 0
invldinp = 0
while (True):
    usrinp = input("Enter your choice, Press S for snake W for water and G for gun:\n")
    if usrinp == "G" and computerchoice == "Gun":
        print("Draw!")
        d = d+1
        n = n-1
        if n == 0:
            print("Maximum number reached, Game over!")
            break
        continue
    elif usrinp == "G" and computerchoice == "Water":
        print("You lost!")
        l = l+1
        n = n-1
        if n == 0:
            print("Maximum number reached, Game over!")
            break
        continue
    elif usrinp == "G" and computerchoice == "Snake":
        print("You Won!")
        w = w+1
        n = n-1
        if n == 0:
            print("Maximum number reached, Game over!")
            break
        continue
    elif usrinp == "S" and computerchoice == "Snake":
        print("Draw")
        d = d+1
        n = n-1
        if n == 0:
            print("Maximum number reached, Game over!")
            break
        continue
    elif usrinp == "S" and computerchoice == "Water":
        print("You Won!")
        w = w+1
        n = n-1
        if n == 0:
            print("Maximum number reached, Game over!")
            break
        continue
    elif usrinp == "S" and computerchoice == "Gun":
        print("You lost")
        l = l+1
        n = n-1
        if n == 0:
            print("Maximum number reached, Game over!")
            break
        continue
    elif usrinp == "W" and computerchoice == "Water":
        print("Draw")
        d = d+1
        n = n-1
        if n == 0:
            print("Maximum number reached, Game over!")
            break
        continue
    elif usrinp == "W" and computerchoice == "Gun":
        print("You Won!")
        w = w+1
        n = n-1
        if n == 0:
            print("Maximum number reached, Game over!")
            break
        continue
    elif usrinp == "W" and computerchoice == "Snake":
        print("You lost")
        l = l+1
        n = n-1
        if n == 0:
            print("Maximum number reached, Game over!")
            break
        continue
    elif usrinp!= "G" and "S" and "W":
        print("Enter valid choice")
        invldinp = invldinp + 1
        n = n-1
        if n == 0:
            print("Maximum number reached, Game over!")
            break
        continue
print(f"Maximum level reached and you won {w} times, computer won {l} times, {d} times game draw and you enter"
      f" {invldinp} times wrong input.")
