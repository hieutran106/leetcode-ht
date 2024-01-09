import unittest
from .solution import Solution
from typing import List


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        return 0


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.getLengthOfOptimalCompression(s="aaabcccd", k=2)
        self.assertEqual(4, actual)

    def test_case_2(self):
        actual = self.s.getLengthOfOptimalCompression(s="aabbaa", k=2)
        self.assertEqual(2, actual)

    def test_case_3(self):
        actual = self.s.getLengthOfOptimalCompression(s="aaaaaaaaaaa", k=0)
        self.assertEqual(3, actual)


if __name__ == '__main__':
    unittest.main()
