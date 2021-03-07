import unittest
import fizzbuzz


class TestCase(unittest.TestCase):

  def test_fizzbuzz(self):
    self.assertEqual(fizzbuzz.fun(0), 0) #should throw an error as it's out of the range of numbers

  def test_fizzbuzz1(self):
    self.assertEqual(fizzbuzz.fun(15), fizzbuzz) #Should pass the test as 15 is divisible by 3 and 5

if __name__ == '__main__':
  unittest.main(verbosity=2)
