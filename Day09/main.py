#You can find the puzzle here: https://adventofcode.com/2020/day/9

import sys

#The file containing every numbers
filename = sys.argv[-1]

# =====================
#        PART 1
# =====================

#Find the wrong number
def find_wrong_number(max_nums, number_list):
    numbers_to_check = []
    for i in range(0, len(number_list)):
        if len(numbers_to_check) < max_nums:
            numbers_to_check.append(number_list[i])
        else:
            if check_number(numbers_to_check, number_list[i])[0]:
                numbers_to_check.pop(0)
                numbers_to_check.append(number_list[i])
            else:
                return check_number(numbers_to_check, number_list[i])[1]

#Check if a number is the sum of two numbers in a given list
def check_number(numbers, number_to_check):
    for x in numbers:
        for y in numbers:
            if x != y and x + y == number_to_check:
                return (True, 0)
    return (False, number_to_check)

#Get the expenses and put it in an array
def get_numbers():
    with open(filename) as f:
        listExpenses = f.read().splitlines()
        return list(map(int, listExpenses))


print(find_wrong_number(25, get_numbers()))


# =====================
#        PART 2
# =====================

#Find a list of continuous number equal to the wrong number, then returns the sum of its biggest and smallest number
def fix_wrong_number(wrong_number, number_list):
    my_wrong_number = wrong_number
    my_number_list = number_list
    for i in range(0, len(my_number_list)):
        current_number_list = []
        current_number_list.append(my_number_list[i])
        my_number_target = my_number_list[i]
        current_number_list.append(my_number_list[i])
        for j in range(i + 1, len(my_number_list)):
            if i != j:
                my_number_target += my_number_list[j]
                current_number_list.append(my_number_list[j])
            if my_number_target == my_wrong_number:
                current_number_list.sort()
                return current_number_list[0] + current_number_list[-1]
            elif my_number_target > wrong_number:
                break

print(fix_wrong_number(find_wrong_number(25, get_numbers()), get_numbers()))