import unittest
from typing import List

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return 0
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.countOfSubstrings(word = "aeioqq", k = 1)
        self.assertEqual(actual, 0)
        
    def test_case_2(self):
        actual = self.s.countOfSubstrings(word = "aeiou", k = 0)
        self.assertEqual(actual, 1)

    def test_case_3(self):
        actual = self.s.countOfSubstrings(word = "ieaouqqieaouqq", k = 1)
        self.assertEqual(actual, 3)

    def test_case_4(self):
        actual = self.s.countOfSubstrings(word = "ieaouqi", k = 1)
        self.assertEqual(actual, 2)

if __name__ == '__main__':
    unittest.main()

