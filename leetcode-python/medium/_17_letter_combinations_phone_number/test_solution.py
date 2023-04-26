import unittest
from typing import List

from .solution import Solution


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        def backtrack(i: int, path: List[str]):
            if i >= len(digits):
                res.append(''.join(path))
                return
            choices = phone[digits[i]]
            for c in choices:
                path.append(c)
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return res


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.letterCombinations(digits="23")
        self.assertEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], actual)

    def test_case_2(self):
        actual = self.s.letterCombinations(digits="")
        self.assertEqual([], actual)


if __name__ == '__main__':
    unittest.main()
