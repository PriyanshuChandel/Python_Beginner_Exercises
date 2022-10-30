from random import randint

print('Welcome to Guess Game!')
player1_name = input('Enter player-1 name:\n')
player2_name = input('Enter player-2 name:\n')
while True:
    first_number = int(input(f'{player1_name}, Please enter first number:'))
    second_number = int(input(f'{player1_name}, Please enter second number:'))
    random_number = randint(first_number, second_number)
    player1_try = 0
    player2_try = 0
    player1_guess = int(input(f'{player1_name} please guess the number!\n'))
    if player1_guess > random_number:
        print('You guessed greater number, try again!')
        player1_try = player1_try + 1
        continue
    elif player1_guess < random_number:
        player1_try = player1_try + 1
        print('You guessed lesser number, try again!')
        continue
    elif player1_guess == random_number:
        player1_try = player1_try + 1
        print(f"Correct guess! you took {player1_try} tries..Now it is {player2_name}'s turn")
    first_number2 = int(input(f'{player2_name}, Please enter first number:'))
    second_number2 = int(input(f'{player1_name}, Please enter second number:'))
    random_number2 = randint(first_number2, second_number2)
    while True:
        player2_guess = int(input(f'{player2_name} please guess the number!\n'))
        if player2_guess > random_number2:
            player2_try = player2_try + 1
            print('You guessed greater number, try again!')
            continue
        elif player2_guess < random_number2:
            player2_try = player2_try + 1
            print('You guessed lesser number, try again!')
            continue
        elif player2_guess == random_number2:
            player2_try = player2_try + 1
            print(f"Correct guess! you took {player2_try} tries..\n")
            break
    if player1_try > player2_try:
        print(f'{player2_name} took {player2_try} tries...won the game!')
    elif player2_try > player1_try:
        print(f'{player1_name} took {player1_try} tries...won the game!')
    elif player2_try == player1_try:
        print("Match DRAW!")
    user_inp = input(f'Enter "Q" to quite or "C" to continue to play again:').capitalize()
    if user_inp == "Q":
        break
    if user_inp == "C":
        continue
    break
