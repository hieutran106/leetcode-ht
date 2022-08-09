import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        s = Solution()
        actual = s.finalPrices([8,4,6,2,3])
        self.assertCountEqual(actual, [4,2,4,2,3])

    def test_case_2(self):
        s = Solution()
        actual = s.finalPrices([1,2,3,4,5])
        self.assertCountEqual(actual, [1,2,3,4,5])

    def test_case_3(self):
        s = Solution()
        actual = s.finalPrices([10,1,1,6])
        self.assertCountEqual(actual, [9,0,1,6])


if __name__ == '__main__':
    unittest.main()
