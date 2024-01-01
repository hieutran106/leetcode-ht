import unittest
from .solution import Solution
from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        counter_matrix = [[0 for _ in range(26)] for _ in range(n)]
        for (row, word) in enumerate(words):
            for c in word:
                col = ord(c) - ord('a')
                counter_matrix[row][col] += 1
        for c in range(26):
            col_sum = 0
            for r in range(n):
                col_sum += counter_matrix[r][c]
            if col_sum % n != 0:
                return False
        return True

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.makeEqual(words = ["abc","aabc","bc"])
        self.assertEqual(True, actual)
        
    def test_case_2(self):
        actual = self.s.makeEqual(words = ["ab","a"])
        self.assertEqual(False, actual)

    def test_case_3(self):
        actual = self.s.makeEqual(words = ["aaaa","bbbb"])
        self.assertEqual(True, actual)

    def test_case_4(self):
        actual = self.s.makeEqual(words = ["aaaa","bbbb", "c"])
        self.assertEqual(False, actual)

if __name__ == '__main__':
    unittest.main()

