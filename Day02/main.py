#You can find the puzzle here: https://adventofcode.com/2020/day/2

import sys

#The file containing every inputs
filename = sys.argv[-1]

# =====================
#        PART 1
# =====================

#Sorting valid inputs
def SortValidInputs():
    allInputs = GetInputs()
    validInputs = []
    for i in allInputs:
        if IsValidInput(i[0], i[1], i[2], i[3]):
            validInputs.append(i)
    return validInputs

#Checking if an input is valid
def IsValidInput(min, max, letter, password):
    occurences = password.count(letter)
    if occurences >= min and occurences <= max:
        return True
    else:
        return False

#Getting the inputs from a txt file
def GetInputs():
    with open(filename) as f:
        listInputs = f.read().splitlines()
        myHashedInputs = []
        for i in listInputs:
            splitInput = i.split()
            splitNumbers = splitInput[0].split('-')
            myHashedInputs.append([int(splitNumbers[0]), int(splitNumbers[1]), splitInput[1][0], splitInput[2]])
        return myHashedInputs


print(len(SortValidInputs()))


# =====================
#        PART 2
# =====================

#Sorting valid inputs
def SortValidInputsV2():
    allInputs = GetInputs()
    validInputs = []
    for i in allInputs:
        if IsValidInputV2(i[0] - 1, i[1] - 1, i[2], i[3]):
            validInputs.append(i)
    return validInputs

#Checking if an input is valid
def IsValidInputV2(firstPos, secondPos, letter, password):
    isInFirstPos =  password[firstPos].find(letter)
    isInSecondPos =  password[secondPos].find(letter)
    if isInFirstPos and not isInSecondPos or not isInFirstPos and isInSecondPos:
        return True
    else:
        return False


print(len(SortValidInputsV2()))