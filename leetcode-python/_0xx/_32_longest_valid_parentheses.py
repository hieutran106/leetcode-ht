import unittest
from typing import List

# Date: 2026-10-08
# Problem: 32 longest_valid_parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open_parent = [0] * len(s)
        close_parent = [0] * len(s)
        for i, c in enumerate(s):
            if i == 0:
                if c == '(':
                   open_parent[i] = 1
                else:
                    close_parent[i] = 1
                continue

            if c == '(':
                open_parent[i] = open_parent[i-1] + 1
                close_parent[i] = close_parent[i-1]
            else:
                open_parent[i] = open_parent[i-1]
                close_parent[i] = close_parent[i-1] + 1

        print(open_parent)
        print(close_parent)
        ans = 0
        for i in range(len(s) - 1):
            for j in range(i+1, len(s)):
                if s[i] == "(" and s[j] ==")":
                    open_count = open_parent[j] - open_parent[i]
                    close_count = close_parent[j] - close_parent[i]
                    if open_count == close_count:
                        print(f"Valid parent substring {i=},{j=}, {open_count=}")
                        ans = max(ans, j - i + 1)

        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.longestValidParentheses(s = "(()")
        self.assertEqual(2, actual)
        
    def test_case_2(self):
        actual = self.s.longestValidParentheses(s = ")()())")
        self.assertEqual(4, actual)

    def test_case_3(self):
        actual = self.s.longestValidParentheses(s = "")
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.longestValidParentheses(s = ")((()))()((()")
        self.assertEqual(8, actual)

if __name__ == '__main__':
    unittest.main()

