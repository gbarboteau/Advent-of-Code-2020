#You can find the puzzle here: https://adventofcode.com/2020/day/6

import sys
import math

#The file containing every inputs
filename = sys.argv[-1]

# =====================
#        PART 1
# =====================

#Get the number of question anyone answered "yes"
def GetNumberOfAnswers():
    numberOfAnswers = []
    allAnswers = GetAnswers()
    for a in allAnswers:
        numA = len("".join(set(a)).replace(" ", ""))
        numberOfAnswers.append(numA)
    return numberOfAnswers

#Getting the inputs from a txt file
def GetAnswers():
    listAnwers = []
    hashedAnwers = []
    with open(filename) as f:
        listAnwers = f.read().split("\n\n")
    for c in listAnwers:
        pc = c.replace("\n", " ")
        hashedAnwers.append(pc)
    return hashedAnwers


print(sum(GetNumberOfAnswers()))


# =====================
#        PART 2
# =====================

#Get the number of question everyone answered "yes"
def GetNumberOfAnswersV2():
    numberOfAnswers = []
    allAnswers = GetAnswersV2()
    for a in allAnswers:
        numA = set(a[0])
        for i in range(1, len(a)):
            if a[i] != "":
                numA = list(set(numA)&set(a[i]))
        numberOfAnswers.append(len(''.join(numA)))
    return numberOfAnswers

#Getting the inputs from a txt file (varies from the previous version to separates the different persons among a given group)
def GetAnswersV2():
    listAnwers = []
    hashedAnwers = []
    with open(filename) as f:
        listAnwers = f.read().split("\n\n")
    for c in listAnwers:
        pc = c.split("\n")
        hashedAnwers.append(pc)
    return hashedAnwers


print(sum(GetNumberOfAnswersV2()))