# Long Problem Generator
# The Long Problem Generator will give you a randomly generated long addition, subtraction, multiplication or division problem. You pick the operator you want to work with and the difficulty.
# Author: Aaron Haines
# Date: 23-July-2015
# Copyright: CC BY-NC-SA 4.0

import random
play = "true"
print "Welcome to the Long Problem Generator"
print "Enter your preferred OPERATOR and DIFFICULTY"

def pick():
    operator = raw_input('\nOPERATOR (+ - x or /): ')
    if operator == " ":
        operator = "+"
    difficulty = int(raw_input('\nDIFFICULTY (1=easy 2=medium 3=hard): '))
    return operator, difficulty

def generate(oper, diff):
    print "Generating...\n"
    list = []
    while len(list) < diff + 3:
       list.append(random.randrange(1,10))

    if list[0] < list[1]:
        num = list[0]
        list[0] = list[1]
        list[1] = num
    if list[0] == list[1] and list[2] < list[3]:
        num = list[2]
        list[2] = list[3]
        list[3] = num

    for i in range(0, len(list)):
        list[i] = str(list[i])

    if oper != "+" and operator != "-" and operator != "x" and operator != "/":
        print "...pick one of the operators.\n"
        return
    elif diff == 1 and oper != "/":
        print "   " + list[0] + list[2]
        print " " + oper + " " + list[1] + list[3]
        print "______\n"
    elif diff == 2 and oper != "/":
        print "   " + list[0] + list[2] + list[4]
        print " " + oper + "  " + list[1] + list[3]
        print "______\n"
    elif diff == 3 and oper != "/":
        print "   " + list[0] + list[2] + list[4]
        print " " + oper + " " + list[1] + list[3] + list[5]
        print "______\n"
    elif oper == "/":
        if diff == 1:
            print "   ____"
            print " " + list[1] + " \\ " + list[0] + list[2] + "\n"
        elif diff == 2:
            print "   ______"
            print " " + list[1] + " \\ " + list[0] + list[2] + list[3] + list[4] + "\n"
        elif diff == 3:
            print "    ______"
            print " " + list[1] + list[4] + " \\ " + list[0] + list[2] + list[3] + list[5] + "\n"
    else:
        print "...pick a difficulty from 1 to 3.\n"

def again():
    answer = raw_input('Generate another? (y or n): ')
    if answer == 'y':
        return "true"
    elif answer == 'n':
        return "false"
    else:
        return "true"

while play == "true":
    operator, difficulty = pick()
    generate(operator,difficulty)
    play = again()

print "Goodbye."
