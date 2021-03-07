import unittest

def fun(x):
    if x < 1 or x > 100:
        return "Invalid Input"
    if x % 3 == 0:
        if x % 5 == 0:
            return "FizzBuzz"
        else:
            return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x
