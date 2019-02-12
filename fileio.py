import random
import sys
import os

test_file = open("testfile.txt", "wb")

print(test_file.mode)

print(test_file.name)

test_file.write(bytes("Lines written by SKK\n", 'UTF-8'))

test_file.close()

test_file = open("testfile.txt", "r+")

text_in_file = test_file.read()

print(text_in_file)

test_file.close()


# os.remove("testfile.txt")
