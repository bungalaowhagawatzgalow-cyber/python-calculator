
import time
from math import sqrt, cbrt, pi


def _ready():
    operators = {  # to simplify
        "+": lambda n1, n2: n1 + n2,
        "-": lambda n1, n2: n1 - n2,
        "*": lambda n1, n2: n1 * n2,
        "/": lambda n1, n2: n1 / n2,
        "**": lambda n1, n2: n1 ** n2,
        "sqrt": lambda n1, n2: sqrt(n1),
        "cbrt": lambda n1, n2: cbrt(n1),
        "PI": lambda n1, n2: n1 * pi,
		"%": lambda n1, n2: (n1 / n2) * 100
    }

    listoperations = {  # list of operators to show at the start
        "+",
        "-",
        "*",
        "/",
        "**",
        "sqrt",
        "cbrt",
        "PI"
    }

    print("List of valid operators: " + str(listoperations))

    percentagemode = input("Percentage Mode (yes/no) = ")  # asks whether or not you want percents

    while percentagemode.lower() != "no" and percentagemode.lower() != "yes":  #.lower() is used so regardless if its YES or yEs it will still accept it
        print("Try again!")  # if code above is true then it asks you to try again
        percentagemode = input("Percentage Mode (yes/no) = ")

    if percentagemode.lower() == "yes":  # if percentagemode is true/yes then it will ask for % only
        op = input("Operator (% only) = ")
    else:  # else it doesnt and goes to normal
        op = input("Operator = ")

    while True:
        while op not in operators:
            print("Try again!")
            op = input("Operator = ")  # if you do not put an operator in the list it will ask again

        try:
            n1 = float(input("First Number = "))

            if op not in ("sqrt", "cbrt", "PI"):  # if neither of these are used, then will allow for a second number
                n2 = float(input("Second Number = "))

            break

        except ValueError:
            print("Not a valid number! Try again.")

    # base code below

    while op == "/" and n2 == 0:  # checks for division by 0
        print("Not divisible by zero")
        n2 = float(input("Second Number = "))

    if percentagemode.lower() == "no":  # if the value is true then it will do normal arithmetic
        if op in operators:
            if op in ("sqrt", "cbrt", "PI"):  # if its any of these numbers then it wont ask for a seconnd number
                result = operators[op](n1, None)
            else:
                result = operators[op](n1, n2)
        else:
            print("Invalid operator!")
            return

    elif percentagemode.lower() == "yes":  # if its false then it will do percentage calculations
        if op == "%":
            print("Second Number is percentage")
            time.sleep(2.5)
            result = (n1 * n2) / 100  # n2 calculates the percentage of n1. for eg: if you type n1 as 25 and n2 as 12 it will take 12% of 25
        else:
            print("Didnt put a percentage")

    # shows the result after calculation
    print("Calculation finished!")
    time.sleep(.5)
    print("result = ", result)

    endprogram = input("Continue? (yes/no) = ")  # if yes it will end if no it will continue with another calculation

    if endprogram.lower() == "yes":
        _ready()
    elif endprogram.lower() == "no":
        print("See you next time!")
        exit()


startprogram = input("Start calculator (yes/no) = ")

if startprogram.lower() == "yes":  # asks if you want to start or not
    _ready()
elif startprogram.lower() == "no":
    print("See you next time!")
    exit()
