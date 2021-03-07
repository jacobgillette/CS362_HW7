import unittest
import leapyear

class TestCase(unittest.TestCase):

    def test_leapyear(self):
        self.assertEqual(leapyear.fun(0), "Invalid Input") #should throw an error as it's out of the range of numbers

    def test_leapyear1(self):
        self.assertEqual(leapyear.fun(4), "Input is a leap year") #Return as a leap year

    def test_leapyear2(self):
        self.assertEqual(leapyear.fun(100), "Input is not a leap year") #Return as not a leap year

    def test_leapyear3(self):
        self.assertEqual(leapyear.fun(400), "Input is a leap year") #Return as a leap year

if __name__ == '__main__':
  unittest.main(verbosity=2)
