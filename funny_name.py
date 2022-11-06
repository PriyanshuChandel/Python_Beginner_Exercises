"""
*It's result day at school and not everyone is happy.
*You decided to make your friends laugh by jumbling their names to come up with some funny names.
*Your program should take the number of names and the names separated by space as input.
*Output should be funny names in the same order.

Input:
Enter number of friends:
3
Enter the name of your 3 friends:
Rohan Das,Shubham Agarwal,Ritesh Arora

Output:
Ritesh Das
Shubham Arora
Rohan Agarwal
"""

from random import choice


def funny_names(lisst):
    name_list = [name.strip().split(' ', 1)[0] for name in lisst]
    surname_list = [surname.strip().split(' ', 1)[1] for surname in lisst]
    for name in name_list:
        print(f'{name} {choice(surname_list)}')


if __name__ == "__main__":
    number_friends = input('Enter number of friends: ')
    try:
        number_friends = int(number_friends)
        name_friends = input(f'Enter name of {number_friends} friends separated by comma\n:')
        friend_list = name_friends.split(',')
        if len(friend_list) > number_friends:
            print(f'You enter {len(friend_list) - number_friends} more friends.')
        if len(friend_list) < number_friends:
            print(f'You enter {number_friends - len(friend_list)} less friends.')
        if len(friend_list) == number_friends:
            funny_names(friend_list)
    except:
        print('Please enter valid number')
