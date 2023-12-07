import unittest
from .solution import Solution
from typing import List


class Solution:
    def largestOddNumber(self, num: str) -> str:
        odds = {"1", "3", "5", "7", "9"}
        for i in range(len(num) -1, -1, -1):
            if num[i] in odds:
                return num[0:i + 1]
        return ""
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.largestOddNumber(num = "52")
        self.assertEqual("5", actual)
        
    def test_case_2(self):
        actual = self.s.largestOddNumber(num = "4206")
        self.assertEqual("", actual)

    def test_case_3(self):
        actual = self.s.largestOddNumber(num = "35427")
        self.assertEqual("35427", actual)

    def test_case_4(self):
        actual = self.s.largestOddNumber(num = "30924")
        self.assertEqual("309", actual)

if __name__ == '__main__':
    unittest.main()

