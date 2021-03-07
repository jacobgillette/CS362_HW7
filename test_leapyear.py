import unittest
import leapyear

class TestCase(unittest.TestCase):

    def test_leapyear(self):
        self.assertEqual(leapyear.fun(0), "Invalid Input") #should throw an error as it's out of the range of numbers

    def test_leapyear1(self):
        self.assertEqual(leapyear.fun(4), "Leap year") #should throw an error as it's out of the range of numbers


if __name__ == '__main__':
  unittest.main(verbosity=2)
