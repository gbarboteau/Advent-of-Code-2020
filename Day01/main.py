#You can find the puzzle here: https://adventofcode.com/2020/day/1

import math
import sys

#The file containing every masses
filename = sys.argv[-1]
target = 2020

# =====================
#        PART 1
# =====================

#Multiply the two numbers that make 2020
def GetTheSum():
    nums = GetTheTwoNumbers()
    mySum = nums[0] * nums[1]
    return mySum 

#Find the two numbers that make 2020
def GetTheTwoNumbers():
    listExpenses = GetExpenses()
    num1 = 0
    num2 = 0
    while num2 == 0:
        for e in listExpenses:
            num1 = e
            myTarget = 2020 - e
            if myTarget in listExpenses:
                num2 = myTarget
                return (num1, num2)
    return (num1, num2)

#Get the expenses and put it in an array
def GetExpenses():
    with open(filename) as f:
        listExpenses = f.read().splitlines()
        return list(map(int, listExpenses))

print(GetTheSum())


# =====================
#        PART 2
# =====================

#Multiply the three numbers that make 2020
def GetTheSumV2():
    nums = GetTheThreeNumbers()
    mySum = nums[0] * nums[1] * nums[2]
    return mySum 

#Find the three numbers that make 2020
def GetTheThreeNumbers():
    listExpenses = GetExpenses()
    num1 = 0
    num2 = 0
    num3 = 0
    while num3 == 0:
        for e in listExpenses:
            num1 = e
            myFirstTarget = target - e
            for f in listExpenses: 
                num2 = f
                mySecondTarget = myFirstTarget - f
                if mySecondTarget in listExpenses:
                    num3 = mySecondTarget
                    return (num1, num2, num3)
    return (num1, num2, num3)

print(GetTheSumV2())