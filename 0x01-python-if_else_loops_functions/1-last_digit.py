#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_num = repr(number)
last_dig = str_num[-1]
last_num = int(last_dig)
if (last_num > 5):
    print("Last digit of {} is {} and is greater than 5".format(number,last_num))
if (last_num == 0):
    print("Last digit of {} is {} and is zero".format(number,last_num))
else:
   print("Last digit of {} is {} and is less than 6 and not 0".format(number,last_num))
