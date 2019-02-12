import random
import sys
import os

age = 64

if age > 16:
    print("You're old enough to drive")
else:
    print("You're not old enough to drive")

if age >= 21:
    print("You're old enough to drive a tractor trailer")
elif age >= 16:
    print('You\'re old enough to drive a car')
else:
    print("You're not old enough to drive")

if 1 <= age <= 18:
    print("You get a birthday party")
elif age <= 21 or age >= 65:
    print("You're going to get a present")
else:
    print("You've to give the birthday party")
