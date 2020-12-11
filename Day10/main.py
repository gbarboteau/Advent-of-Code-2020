#You can find the puzzle here: https://adventofcode.com/2020/day/10

import sys

#The file containing every numbers
filename = sys.argv[-1]

# =====================
#        PART 1
# =====================

#Count the number of different jolt differences
def count_jolt_differences(adaptaters_list):
    jolt_dif_list = [0, 0, 0]
    my_adaptaters_list = adaptaters_list
    my_adaptaters_list.sort()
    my_adaptaters_list.insert(0, 0)
    my_adaptaters_list.append(my_adaptaters_list[-1] +3)
    for i in range(0, len(my_adaptaters_list) -1):
        my_diff = my_adaptaters_list[i +1] - my_adaptaters_list[i]
        if my_diff >= 1 and my_diff <= 3:
            jolt_dif_list[my_diff -1] += 1
    return jolt_dif_list

#Get the expenses and put it in an array
def get_adaptaters():
    with open(filename) as f:
        listExpenses = f.read().splitlines()
        return list(map(int, listExpenses))


print(count_jolt_differences(get_adaptaters())[0] * count_jolt_differences(get_adaptaters())[2])
