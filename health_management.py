# Create a health management software
# 3 clients are - harry, rohan, hammad
# create 3 files for food records
# create 3 files for exercise
# ask either wants to log or retrieve
# write a function which takes client name as input like press 1 for rohan, 2 for harry 3 for hammad
# then may be 1 for exercise and 2 for diet
# use below function
# take time by using below function
"""
def getdate():
    import datetime
    return datetime.datetime.now()
"""

# Solution
# file tut32_harry_exercise.txt, tut32_harry_diet.txt, tut32_rohan_exercise.txt, tut32_rohan_diet.txt, tut32_hammad_exercise.txt and tut32_hammad_diet.txt created for this purpose.
# below strings are created just not type everytime.
lastmess1 = "Congratulations! You've logged your exercise details successfully."
lastmess2 = "Congratulations! You've logged your diet details successfully."
lastmess3 = "Enter valid input."
commoninput1 = "Enter 1 to log exercise details or 2 for diet details:\n"
commoninput2 = "enter you exercise details:\n"
commoninput3 = "enter you diet details:\n"
commoinput4 = "Enter 1 to retrieve exercise details or 2 for diet details:\n"
commoinput5 = "here is your exercise details:\n"
commoinput6 = "here is your diet details:\n"


# actual program starts from here
def getdate():
    import datetime
    return datetime.datetime.now()

input1 = int(input("Welcome to fitness club!\nEnter 1 to log details or 2 to retrieve details:\n"))
if input1 == 1:
    input2 = int(input("Welcome to health management log system!\n"
                       "Please press 1 for Harry, 2 for Rohan and 3 for Hammad:\n"))
    if input2 == 1:
        input3 = int(input(commoninput1))
        if input3 == 1:
            print("Hi Harry", commoninput2)
            f = open("tut32_harry_exercise.txt", "a")
            f.write(str(getdate()) + " " + input() + "\n")
            print(lastmess1)
            f.close()
        elif input3 == 2:
            print("Hi Harry", commoninput3)
            f = open("tut32_harry_diet.txt", "a")
            f.write(str(getdate()) + " " + input() + "\n")
            print(lastmess2)
            f.close()
        else:
            print(lastmess3)
    elif input2 == 2:
        input4 = int(input(commoninput1))
        if input4 == 1:
            print("Hi Rohan", commoninput2)
            f = open("tut32_rohan_exercise.txt", "a")
            f.write(str(getdate()) + " " + input() + "\n")
            print(lastmess1)
            f.close()
        elif input4 == 2:
            print("Hi Rohan", commoninput3)
            f = open("tut32_rohan_diet.txt", "a")
            f.write(str(getdate()) + " " + input() + "\n")
            print(lastmess2)
            f.close()
        else:
            print(lastmess3)
    elif input2 == 3:
        input5 = int(input(commoninput1))
        if input5 == 1:
            print("Hi Hammad", commoninput2)
            f = open("tut32_hammad_exercise.txt", "a")
            f.write(str(getdate()) + " " + input() + "\n")
            print(lastmess1)
            f.close()
        elif input5 == 2:
            print("Hi Hammad", commoninput3)
            f = open("tut32_hammad_diet.txt", "a")
            f.write(str(getdate()) + " " + input() + "\n")
            print(lastmess2)
            f.close()
        else:
            print(lastmess3)
    else:
        print(lastmess3)
elif input1 == 2:
    input6 = int(input("Welcome to health management retrieval system:\nPlease press 1 for Harry, "
                       "2 for Rohan and 3 for Hammad:\n"))
    if input6 == 1:
        input7 = int(input(commoinput4))
        if input7 == 1:
            print("Hi Harry", commoinput5)
            f = open("tut32_harry_exercise.txt", "r")
            for line in f:
                print(line, end="")
            f.close()
        elif input7 == 2:
            print("Hi Harry", commoinput6)
            f = open("tut32_harry_diet.txt", "r")
            for line in f:
                print(line, end="")
            f.close()
        else:
            print(lastmess3)
    elif input6 == 2:
        input8 = int(input(commoinput4))
        if input8 == 1:
            print("Hi Rohan", commoinput5)
            f = open("tut32_Rohan_exercise.txt", "r")
            for line in f:
                print(line, end="")
            f.close()
        elif input8 == 2:
            print("Hi Rohan", commoinput6)
            f = open("tut32_rohan_diet.txt", "r")
            for line in f:
                print(line, end="")
            f.close()
        else:
            print(lastmess3)
    elif input6 == 3:
        input9 = int(input(commoinput4))
        if input9 == 1:
            print("Hi Hammad", commoinput5)
            f = open("tut32_hammad_exercise.txt", "r")
            for line in f:
                print(line, end="")
            f.close()
        elif input9 == 2:
            print("Hi Hammad", commoinput6)
            f = open("tut32_hammad_diet.txt", "r")
            for line in f:
                print(line, end="")
            f.close()
        else:
            print(lastmess3)
else:
    print(lastmess3)
