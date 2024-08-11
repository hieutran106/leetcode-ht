import unittest
from typing import List
from functools import cache

class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_right_counts = [0] * len(s)
        for i in range(len(s) -2, -1, -1):
            if s[i+1] == 'a':
                a_right_counts[i] = a_right_counts[i+1] +1
            else:
                a_right_counts[i] = a_right_counts[i+1]
        b_left_count = 0
        ans = float("infinity")
        for i in range(len(s)):
            if i > 0 and s[i-1] == 'b':
                b_left_count += 1
            # number of deletions at index ith to make string balanced
            deletion_count = b_left_count + a_right_counts[i]
            ans = min(ans, deletion_count)
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.minimumDeletions(s="aababbab")
        self.assertEqual(2, actual)

    def test_case_2(self):
        actual = self.s.minimumDeletions(s="bbaaaaabb")
        self.assertEqual(2, actual)

    def test_case_3(self):
        actual = self.s.minimumDeletions(s="a")
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.minimumDeletions(s="bbbbbbbbbbbbbbb")
        self.assertEqual(0, actual)

    def test_case_5(self):
        actual = self.s.minimumDeletions(s="baababbaabbaaabaabbabbbabaaaaaabaabababaaababbb")
        self.assertEqual(18, actual)


if __name__ == '__main__':
    unittest.main()
