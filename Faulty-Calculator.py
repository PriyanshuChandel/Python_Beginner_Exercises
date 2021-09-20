# Exercise - 2, Faulty Calculator
# design a calculator which will correctly solve all calculation except following one.
# 45*3 = 555, 56+9 = 77, 56/6 = 4
# take input as operator and two numbers from user and return the result
#import operator
input1 = int(input("Enter first number:"))
input2 = input("Enter operator, i.e '+', '-', '*', '/':")
input3 = int(input("Enter second number:"))
if input1 == 45 and input2 == "*" and input3 == 3:
    print("Output is", 555)
elif input1 == 56 and input2 == "+" and input3 == 9:
    print("Output is", 77)
elif input1 == 56 and input2 == "/" and input3 == 6:
    print("Output is", 4)
elif input1 == int and input2 == "-" and input3 == int:
    print("Output is", input1 - input3)
elif input2 == "*":
    print(input1 * input3)
elif input2 == "+":
    print(input1 + input3)
elif input2 == "/":
    print(input1 / input3)
elif input2 == "-":
    print(input1 - input3)
else:
    print("Invalid input!, pagal hai kya")
