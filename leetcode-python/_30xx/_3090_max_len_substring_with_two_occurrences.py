import collections
import unittest
from operator import truediv
from typing import List

# Date: 2026-08-18
# Problem: 3090 max_len_substring_with_two_occurrences
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = collections.defaultdict(int)
        ans, l = 0, 0

        for r, ch in enumerate(s):
            freq[ch] += 1
            while freq[ch] > 2:
                freq[s[l]] -= 1
                l += 1
            ans = max(ans, r -l +1)
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.maximumLengthSubstring(s = "bcbbbcba")
        self.assertEqual(4, actual)
        
    def test_case_2(self):
        actual = self.s.maximumLengthSubstring(s="aaaa")
        self.assertEqual(2, actual)

    def test_case_3(self):
        actual = self.s.maximumLengthSubstring(s="acacbbacbbbxyzxyzuuu")
        self.assertEqual(10, actual)

if __name__ == '__main__':
    unittest.main()

