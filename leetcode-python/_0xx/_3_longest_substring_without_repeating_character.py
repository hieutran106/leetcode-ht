import collections
import unittest
from typing import List, Dict

# 2025-03-13
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def is_valid_window(c: Dict):
            for v in c.values():
                if v > 1:
                    return False
            return True
        ans = 0
        l = 0
        counter = collections.defaultdict(int)
        for r in range(len(s)):
            counter[s[r]] += 1
            while not is_valid_window(counter):
                counter[s[l]] -=1
                l += 1
            ans = max(ans, r-l + 1)
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.lengthOfLongestSubstring(s = "abcabcbb")
        self.assertEqual(3, actual)

    def test_case_2(self):
        actual = self.s.lengthOfLongestSubstring("bbbbb")
        self.assertEqual(1, actual)

    def test_case_3(self):
        actual = self.s.lengthOfLongestSubstring("pwwkew")
        self.assertEqual(3, actual)

    def test_case_4(self):
        actual = self.s.lengthOfLongestSubstring("abcdefcabxyz")
        self.assertEqual(9, actual)

    def test_case_5(self):
        actual = self.s.lengthOfLongestSubstring("")
        self.assertEqual(0, actual)


if __name__ == '__main__':
    unittest.main()
