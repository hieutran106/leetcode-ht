import unittest
from typing import List

# Date: 2025-28-07
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        return 0

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.findTheLongestSubstring(s = "eleetminicoworoep")
        self.assertEqual(13, actual)
        
    def test_case_2(self):
        actual = self.s.findTheLongestSubstring(s = "leetcodeisgreat")
        self.assertEqual(5, actual)

    def test_case_3(self):
        actual = self.s.findTheLongestSubstring(s = "bcbcbc")
        self.assertEqual(6, actual)

if __name__ == '__main__':
    unittest.main()

