import unittest
from typing import List

# Date: 2025-28-07
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # Divide and Conquer
        # Find the invalid char that does not have lower and upper case in s
        # Break into left and right substring at the invalid position
        chars = set(s)
        for i, c in enumerate(s):
            if c.lower() in chars and c.upper() in chars:
                continue
            left = self.longestNiceSubstring(s[:i])
            right = self.longestNiceSubstring(s[i+1:])
            if len(left) >= len(right):
                return left
            return right
        return s

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.longestNiceSubstring(s = "YazaAay")
        self.assertEqual("aAa", actual)
        
    def test_case_2(self):
        actual = self.s.longestNiceSubstring(s = "Bb")
        self.assertEqual("Bb", actual)

    def test_case_3(self):
        actual = self.s.longestNiceSubstring(s = "c")
        self.assertEqual("", actual)

    def test_case_4(self):
        actual = self.s.longestNiceSubstring(s = "zabAABBAdZ")
        self.assertEqual("abAABBA", actual)

    def test_case_5(self):
        actual = self.s.longestNiceSubstring(s = "zabAABBAdZDeeee")
        self.assertEqual("zabAABBAdZD", actual)

    def test_case_6(self):
        actual = self.s.longestNiceSubstring(s = "fzabAABBAdZDeeee")
        self.assertEqual("zabAABBAdZD", actual)

    def test_case_7(self):
        actual = self.s.longestNiceSubstring(s = "aYazAaAy")
        self.assertEqual("AaA", actual)

    def test_case_8(self):
        actual = self.s.longestNiceSubstring(s = "")
        self.assertEqual("", actual)


if __name__ == '__main__':
    unittest.main()

