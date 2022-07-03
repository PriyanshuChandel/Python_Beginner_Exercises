"""
1.A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:
676, 616,100001.
2.You have to take a number as input from the user. You have to find the next palindrome corresponding to that number.
3.Your first input should be the number of test cases and then take all the cases as input from the user.
"""
def palindrome(num):
    num = num + 1
    while not is_palindrome(num):
        num = num + 1
    return num


def is_palindrome(n):
    return str(n) == str(n)[::-1]


number_list = list()
while True:
    how_many = input('Enter how many palindrome you want to check.\n:')
    try:
        int(how_many)
    except Exception as e:
        print(f'SOMETHING WENT WRONG, SEE ERROR BELOW.\n==============================================\n{e}\n'
              f'==============================================')
        continue
    try:
        numbers_to_check = input(f'Enter {how_many} numbers separated by ",".\n:')
        if len(numbers_to_check.split(',')) == int(how_many):
            for entry in numbers_to_check.split(','):
                number_list.append(int(entry))
        else:
            print(f'Entry is restricted to specified range, try again...')
            continue
        print(number_list)
        if len(number_list) == int(how_many):
            for index in range(int(how_many)):
                print(f"Next palindrome for {number_list[index]} is {palindrome(int(number_list[index]))}")
            break
        continue
    except Exception as e:
        print(f'SOMETHING WENT WRONG, SEE ERROR BELOW.\n==============================================\n{e}\n'
              f'==============================================')
        continue
