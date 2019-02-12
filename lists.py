import random
import sys
import os

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = [4, 5, 6]

combo_list = [list1, list2]

print(combo_list)

list1.insert(2, 'd')

print(combo_list)

list2.remove(1)
print(combo_list)

list1.sort()
list2.reverse()

print(combo_list)

merged_list = list2 + list3

print(merged_list)

print(len(merged_list))

print(min(merged_list))

print(max(merged_list))
