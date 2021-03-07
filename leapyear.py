import unittest


def fun(user_in):
    if user_in < 1:
        return "Invalid Input"
    if user_in % 4 == 0:
        if user_in % 100 == 0:
            if user_in % 400 == 0:
                return "Input is a leap year"
            else:
                return "Input is not a leap year"
        else:
            return "Input is a leap year"
    else:
        return "Input is not a leap year"
