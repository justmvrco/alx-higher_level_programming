#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# check for negative numbbers
if number < 0:
    lastDigit = -((-1*number) % 10)
else:
    lastDigit = number % 10

# check the last digit of the number
if lastDigit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, lastDigit))
elif lastDigit > 5:
    print("Last digit of {:d} is {:d} and is greater\
 than 5".format(number, lastDigit))
elif lastDigit < 6 and lastDigit != 0:
    print("Last digit of {:d} is {:d} and is\
 less than 6 and not 0".format(number, lastDigit))
