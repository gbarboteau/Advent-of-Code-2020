#You can find the puzzle here: https://adventofcode.com/2020/day/7

import sys

#The file containing every inputs
filename = sys.argv[-1]

# =====================
#        PART 1
# =====================

#Count the number of shiny gold bags
def CountShinyBags():
    myRegulations = GetRegulations()
    numberShinyBags = 0
    for bag in myRegulations:
        if DoesContainShiny(bag, myRegulations):
            numberShinyBags += 1
    return numberShinyBags

#Check recursively if a given bag contains a shiny gold
def DoesContainShiny(bag, myRegulations):
    containsShiny = False
    if myRegulations[bag]:
        for i in list(set(myRegulations[bag])):
            if i == "shiny gold":
                containsShiny = True
            elif i == "no other bags":
                pass
            elif DoesContainShiny(i, myRegulations) == True:
                    containsShiny = True
    return containsShiny

#Getting the bags regulations from a txt file
def GetRegulations():
    listRegulations = []
    hashedRegulations = {}
    with open(filename) as f:
        listRegulations = f.read().splitlines()
    for c in listRegulations:
        thisBag = {}
        colors = " ".join(c.split()[4:]).replace(".", "").split(",")
        hashedColors = []
        for d in colors:
            if d != "no other bags":
                hashD = d.split()
                for i in range (0, int(hashD[0])):
                    hashedColors.append(" ".join(d.split()[1:3]))
        thisBag[" ".join(c.split()[:2])] = hashedColors
        hashedRegulations.update(thisBag)
    return hashedRegulations


print(CountShinyBags())


# =====================
#        PART 2
# =====================

#Count recursively the total of bags inside a bag
def CountBags(targetBag, regulations):
    numberBags = 0
    for bag in regulations[targetBag]:
        numberBags += 1
        numberBags += CountBags(bag, regulations)
    return numberBags


print(CountBags("shiny gold", GetRegulations()))
