import unittest
from typing import List

from .solution import Solution


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtrack(i: int, path: List[str]):
            if i >= len(s):
                res.append(path.copy())
                return
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    path.append(s[i:j + 1])
                    backtrack(j + 1, path)
                    path.pop()
        backtrack(0, [])
        return res


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.partition(s="aab")
        self.assertEqual([["a", "a", "b"], ["aa", "b"]], actual)

    def test_case_2(self):
        actual = self.s.partition(s="a")
        self.assertEqual([["a"]], actual)


if __name__ == '__main__':
    unittest.main()
