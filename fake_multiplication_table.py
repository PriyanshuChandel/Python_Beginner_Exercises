"""
*Rohan das is a fraud by nature.
*Rohan Das wrote a python function to print a multiplication table of a given number and put one of the values
(randomly generated) as wrong.
*Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!
*So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates
Rohan’s multiplication table.
*Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.
*Note: Rohan’s function returns a list of numbers like this
Rohan Das’s Function Input:
rohanMultiplication(6)
Rohan’s function returns this output:
[6, 12, 18, 26, …., 60]
*You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and
print it to the screen! If the table is correct, your function returns None

"""
from operator import add, sub
from random import randint, choice


def rohan_function(num):
    table = [num * n for n in range(1, 11)]
    table_index = randint(1, 8)
    operators = {'+': add, '-':sub}
    op = choice(list(operators.keys()))
    table[table_index] = operators.get(op)(table[table_index], randint(0,2))
    return table

def isCorrect(table):
    correctTable = [table[0] * n for n in range(1, 11)]
    for correctItem, rohanItem in zip(correctTable, table):
        if correctItem != rohanItem:
            return table.index(rohanItem) + 1


if __name__ == "__main__":
    user_input = int(input('Enter the number for which table need to be checked.\n:'))
    rohanTable = rohan_function(user_input)
    return_index = isCorrect(rohanTable)
    print(rohanTable)
    if  return_index is not None:
        print(f'Rohan made you fool, his program calculated wrong value {rohanTable[return_index-1]} instead of'
              f' {return_index*user_input} at {return_index}th place.')
    else:
        print("Rohan's table is correct")
