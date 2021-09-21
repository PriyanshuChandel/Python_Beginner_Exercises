# Guess game
# take input from user
# inform user number is bigger than 18 or lesser than 18 with number of guess left
# no of guesses should limited to 9
# keep program running until he guessed or 9 attempts fail
# after number of guess over, print game over
# if guess matched to 18, print you won, also print how many attempts he took to win

print("Welcome to guess game!, you will have total 9 attempts left\nGood luck!")
count1 = 8
count2 = 1
while (True):
    n = int(input("Enter your guess:\n"))
    if n < 18:
        print("Input is lesser and you left with", str(count1), "attempts")
        count1 = count1 - 1
        count2 = count2 + 1
        if count1 == -1:
            print("Maximum number reached, Game over!")
            break
        continue
    elif n > 18:
        print("Input is greater and you left with", str(count1), "attempts")
        count1 = count1 - 1
        count2 = count2 + 1
        if count1 == -1:
            print("Maximum number reached and correct number was 18, Game over!")
            break
        continue
    elif n == 18:
        print("You guessed it correctly in", str(count2), "attempts, You won!")
        break
