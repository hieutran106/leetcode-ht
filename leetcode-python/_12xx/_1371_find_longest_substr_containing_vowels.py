import unittest
from typing import List

# Date: 2025-28-07
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0b00000
        visit = {}
        visit[mask] = -1
        ans = 0
        for i, c in enumerate(s):
            if c == 'a':
                mask = mask ^ 0b10000
            elif c == 'e':
                mask = mask ^ 0b01000
            elif c == 'i':
                mask = mask ^ 0b00100
            elif c == 'o':
                mask = mask ^ 0b00010
            elif c == 'u':
                mask = mask ^ 0b00001
            # print(f"Mask at {i=}: mask={bin(mask)}")
            if mask in visit:
                ans = max(ans, i - visit[mask])
            else:
                visit[mask] = i
        return ans
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

    def test_case_4(self):
        actual = self.s.findTheLongestSubstring(s = "oleetcodoccccc")
        self.assertEqual(13, actual)

    def test_case_5(self):
        actual = self.s.findTheLongestSubstring(s = "aeea")
        self.assertEqual(4, actual)

if __name__ == '__main__':
    unittest.main()

