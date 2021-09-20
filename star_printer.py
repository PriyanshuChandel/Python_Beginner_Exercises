# star printer
# input is number input = integer n
# also take a boolean variable, take 0 and 1 as input and set boolean variable true or false
# if boolean is true, print in ascending order else descending order

n1 = int(input("How many time you want to print:\n"))
n2 = bool(int(input("Enter 1 for ascending order, and 0 for descending order:")))
if n2 == True:
    countlines = 0
    while (countlines<=n1):
        print("*" * countlines)
        countlines = countlines + 1
elif n2 == False:
    countlines = n1
    while (countlines > 0):
        print("*" * countlines)
        countlines = countlines - 1
else:
    print("Invalid input")
