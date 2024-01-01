import unittest
from .solution import Solution
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        g_index = 0
        s_index = 0
        while g_index < len(g) and s_index < len(s):
            if s[s_index] >= g[g_index]:
                res += 1
                g_index += 1
            s_index += 1
        return res


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.findContentChildren(g=[1, 2, 3], s=[1, 1])
        self.assertEqual(actual, 1)

    def test_case_2(self):
        actual = self.s.findContentChildren(g=[1, 2], s=[1, 2, 3])
        self.assertEqual(actual, 2)

    def test_case_3(self):
        actual = self.s.findContentChildren(g=[2], s=[1])
        self.assertEqual(actual, 0)

    def test_case_4(self):
        actual = self.s.findContentChildren(g=[9, 1, 9], s=[9, 8, 1])
        self.assertEqual(actual, 2)


if __name__ == '__main__':
    unittest.main()
