#You can find the puzzle here: https://adventofcode.com/2020/day/5

import sys
import math

#The file containing every inputs
filename = sys.argv[-1]

# =====================
#        PART 1
# =====================

#Get All IDs
def GetIDs():
    allIDs = []
    allPositions = GetPositions()
    for p in allPositions:
        allIDs.append(p[0] * 8 + p[1])
    return allIDs

#Get all positions
def GetPositions():
    rowRange = []
    colRange = []
    for i in range(0, 128):
        rowRange.append(i)
    for j in range(0, 8):
        colRange.append(j)
    allPositions = []
    allPasses = GetPasses()
    for s in allPasses:
        allPositions.append(FindSeat(s, rowRange, colRange))
    return allPositions

#Find a given position from a boarding pass
def FindSeat(boardingPass, rowRange, colRange):
    passRow = boardingPass[:-3]
    passCol = boardingPass[-3:]
    finalPosition = [0, 0]
    for i in passRow:
        if i == "F":
            rowRange = rowRange[:int(len(rowRange)/2)]
        elif i == "B":
            rowRange = rowRange[int(len(rowRange)/2):]
    for j in passCol:
        if j == "L":
            colRange = colRange[:int(len(colRange)/2)]
        elif j == "R":
            colRange = colRange[int(len(colRange)/2):]
    finalPosition = [rowRange[0], colRange[0]]
    return finalPosition

#Getting the inputs from a txt file
def GetPasses():
    with open(filename) as f:
        listPasses = f.read().splitlines()
        return listPasses


print(max(GetIDs()))


# =====================
#        PART 2
# =====================

#Find the one seat left in the plane
def FindMySeat():
    allIDs = GetIDs()
    for i in allIDs:
        if i + 1 not in allIDs and i + 2 in allIDs:
            if DoesSeatExist(i):
                return i+1

#Check if the seat exists (not in the front or back row)
def DoesSeatExist(seatID):
    seatID += 1
    myRow = int(seatID / 8)
    if myRow == 0 or myRow == 127:
        return False
    else: 
        return True


print(FindMySeat())