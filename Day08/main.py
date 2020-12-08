#You can find the puzzle here: https://adventofcode.com/2020/day/8

import sys

#The file containing every inputs
filename = sys.argv[-1]

# =====================
#        PART 1
# =====================

def ExecuteUntilLoop(myInstructions):
    accumulator = 0
    currentIndex = 0
    instructionsExecuted = []
    loop = False
    while loop == False:
        if currentIndex in instructionsExecuted:
            loop = True
        else:
            instructionsExecuted.append(currentIndex)
            if myInstructions[currentIndex][0] == "acc":
                accumulator += int(myInstructions[currentIndex][1])
                currentIndex += 1
            elif myInstructions[currentIndex][0] == "jmp":
                currentIndex += int(myInstructions[currentIndex][1])
            elif myInstructions[currentIndex][0] == "nop":
                currentIndex += 1
        if currentIndex >= len(myInstructions):
            return (loop, accumulator)
    return (loop, accumulator)

#Getting the inputs from a txt file
def GetInstructions():
    listInstructions = []
    hashedInstructions = []
    with open(filename) as f:
        listInstructions = f.read().split("\n")
    for c in listInstructions:
        if c:
            pc = c.split()
            hashedInstructions.append(pc)
    return hashedInstructions


print(ExecuteUntilLoop(GetInstructions())[1])


# =====================
#        PART 2
# =====================

def FixLoop(myInstructions):
    for i in range(0, len(myInstructions)):
        newInstructions = myInstructions
        if newInstructions[i][0] == "nop":
            newInstructions[i][0] = "jmp"
        elif newInstructions[i][0] == "jmp":
            newInstructions[i][0] = "nop"
        result = ExecuteUntilLoop(newInstructions)
        if result[0] == False:
            return result[1]
        elif newInstructions[i][0] == "nop":
            newInstructions[i][0] = "jmp"
        elif newInstructions[i][0] == "jmp":
            newInstructions[i][0] = "nop"


print(FixLoop(GetInstructions()))