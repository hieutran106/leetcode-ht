import unittest
from typing import List, TypedDict
import collections


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        dq = collections.deque(s)
        for i in range(len(goal)):
            if "".join(dq) == goal:
                return True
            top = dq.popleft()
            dq.append(top)
        return False


class SolutionBetter:
    def rotateString(self, s: str, goal: str) -> bool:
        # When you concatenate a string with itself (s+s)
        # it contains all possible rotations of the original string
        if len(s) != len(goal):
            return False
        return goal in s + s


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = SolutionBetter()

    def test_case_1(self):
        actual = self.s.rotateString(s="abcde", goal="cdeab")
        self.assertEqual(True, actual)

    def test_case_2(self):
        actual = self.s.rotateString(s="abcde", goal="abced")
        self.assertEqual(False, actual)

    def test_case_3(self):
        actual = self.s.rotateString(s="aaab", goal="aaba")
        self.assertEqual(True, actual)


if __name__ == '__main__':
    unittest.main()
