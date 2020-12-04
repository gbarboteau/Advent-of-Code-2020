#You can find the puzzle here: https://adventofcode.com/2020/day/4

import sys
import re

#The file containing every inputs
filename = sys.argv[-1]


# =====================
#        PART 1
# =====================

#Count the number of valid credentials in a given list
def CountValidCredentials():
    validCredentials = 0
    myCredentials = GetCredentials()
    for c in myCredentials:
        if IsCredentialValid(c):
            validCredentials += 1
    return validCredentials

#Check the validity of a credential
def IsCredentialValid(credential):
    myKeys = credential.keys()
    if "byr" in myKeys and "iyr" in myKeys and "eyr" in myKeys and "hgt" in myKeys and "hcl" in myKeys and "ecl" in myKeys and "pid" in myKeys:
        return True
    else:
        return False

#Getting the inputs from a txt file
def GetCredentials():
    listCredentials = []
    hashedCredentials = []
    with open(filename) as f:
        listCredentials = f.read().split("\n\n")
    for c in listCredentials:
        pc = c.replace("\n", " ").split()
        hc = {}
        for p in pc:
            hc[p.split(":")[0]] = p.split(":")[1]
        hashedCredentials.append(hc)
    return hashedCredentials


print(CountValidCredentials())


# =====================
#        PART 2
# =====================

#Count the number of valid credentials in a given list
def CountValidCredentialsV2():
    validCredentials = 0
    myCredentials = GetCredentials()
    for c in myCredentials:
        if IsCredentialValidV2(c):
            validCredentials += 1
    return validCredentials

#Check the validity of a credential
def IsCredentialValidV2(credential):
    if CheckExistingKeys(credential) and CheckYears(credential) and CheckColorsAndPID(credential) and CheckHeight(credential):
        return True
    else:
        return False

#Check if keys exists in the credential dictionary
def CheckExistingKeys(credential):
    myKeys = credential.keys()
    if "byr" in myKeys and "iyr" in myKeys and "eyr" in myKeys and "hgt" in myKeys and "hcl" in myKeys and "ecl" in myKeys and "pid" in myKeys:
        return True
    else:
        return False

#Check if years are valid
def CheckYears(credential):
    if int(credential["byr"]) >= 1920 and int(credential["byr"]) <= 2002 and int(credential["iyr"]) >= 2010 and int(credential["iyr"]) <= 2020 and int(credential["eyr"]) >= 2020 and int(credential["eyr"]) <= 2030:
        return True
    else:
        return False

#Check if colors and PID are valid
def CheckColorsAndPID(credential):
    if credential["hcl"][0] == "#" and len(credential["hcl"]) == 7 and re.search("[^a-fA-F0-9]", credential["hcl"][1:]) is None and credential["ecl"] in ["amb", "blu" , "brn", "gry", "grn", "hzl", "oth"] and len(credential["pid"]) == 9 and re.search("[^0-9]", credential["pid"]) is None:
        return True
    else:
        return False

#Check if height is valid
def CheckHeight(credential):
    if credential["hgt"][-2:] == "cm" and int(credential["hgt"][:-2]) >= 150 and int(credential["hgt"][:-2]) <= 193 or credential["hgt"][-2:] == "in" and int(credential["hgt"][:-2]) >= 59 and int(credential["hgt"][:-2]) <= 76:
        return True
    else:
        return False


print(CountValidCredentialsV2())