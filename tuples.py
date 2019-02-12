import random
import sys
import os

pi_tuple = (3, 1, 4)

print(pi_tuple)

new_tuple_list = list(pi_tuple)

print(new_tuple_list)

new_tuple_list.append(5)

new_list_tuple = tuple(new_tuple_list)

print(new_list_tuple)
