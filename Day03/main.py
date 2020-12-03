#You can find the puzzle here: https://adventofcode.com/2020/day/3

import sys
import math

#The file containing every inputs
filename = sys.argv[-1]

# =====================
#        PART 1
# =====================

def CountTrees(xMoves, yMoves):
    mySlope = GetSlope()
    lengthLine = len(mySlope[0])
    xCursor = 0
    treesCount = 0
    for yCursor in range(0 + yMoves, len(mySlope), yMoves):
        xCursor += xMoves
        if mySlope[yCursor][xCursor % lengthLine] == '#':
            treesCount += 1
    return treesCount

#Getting the inputs from a txt file
def GetSlope():
    with open(filename) as f:
        listSlope = f.read().splitlines()
        return listSlope


print(CountTrees(3, 1))


# =====================
#        PART 2
# =====================

print(math.prod([CountTrees(1, 1), CountTrees(3, 1), CountTrees(5, 1), CountTrees(7, 1), CountTrees(1, 2)]))