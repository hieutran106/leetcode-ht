import unittest

from utils.my_list import createListFromArray
from .solution import Solution

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        s = Solution()
        input = createListFromArray([1, 0 , 1])
        actual = s.getDecimalValue(input)
        self.assertEqual(actual, 5)

    def test_case_2(self):
        s = Solution()
        input = createListFromArray([0])
        actual = s.getDecimalValue(input)
        self.assertEqual(actual, 0)

    def test_case_3(self):
        s = Solution()
        input = createListFromArray([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0])
        actual = s.getDecimalValue(input)
        self.assertEqual(actual, 18880)

    def test_case_4(self):
        s = Solution()
        input = createListFromArray([0, 0])
        actual = s.getDecimalValue(input)
        self.assertEqual(actual, 0)

    def test_case_5(self):
        s = Solution()
        input = createListFromArray([1])
        actual = s.getDecimalValue(input)
        self.assertEqual(actual, 1)

    def test_case_5(self):
        s = Solution()
        input = createListFromArray([1, 1, 0])
        actual = s.getDecimalValue(input)
        self.assertEqual(actual, 6)


if __name__ == '__main__':
    unittest.main()
