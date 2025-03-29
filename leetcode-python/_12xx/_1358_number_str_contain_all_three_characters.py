import collections
import unittest
from typing import List


class Solution2:
    def numberOfSubstrings(self, s: str) -> int:
        def is_valid_window(d):
            return d['a'] >=1 and d['b'] >=1 and d['c'] >=1;

        l = 0
        ans = 0
        count = collections.defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1
            while is_valid_window(count):
                ans += len(s) - r
                count[s[l]] -= 1
                l+=1

        return ans

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def is_valid_window(d):
            return d['a'] >=1 and d['b'] >=1 and d['c'] >=1;

        ans = 0
        d = collections.defaultdict(int)
        l = 0
        r = 0

        while r < len(s):
            d[s[r]] +=1

            while is_valid_window(d):
                ans += len(s) - r
                d[s[l]] -= 1
                l+= 1
            r+= 1

        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.numberOfSubstrings(s = "abcabc")
        self.assertEqual(10, actual)
        
    def test_case_2(self):
        actual = self.s.numberOfSubstrings(s="aaacb")
        self.assertEqual(3, actual)

    def test_case_3(self):
        actual = self.s.numberOfSubstrings(s="abc")
        self.assertEqual(1, actual)

    def test_case_4(self):
        actual = self.s.numberOfSubstrings(s="abab")
        self.assertEqual(0, actual)

if __name__ == '__main__':
    unittest.main()

