#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
last_digit_with_sign = -last_digit if number < 0 else last_digit

if last_digit_with_sign > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, last_digit_with_sign))
elif last_digit_with_sign == 0:
    print("Last digit of {} is {} and is 0"
          .format(number, last_digit_with_sign))
else:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, last_digit_with_sign))
