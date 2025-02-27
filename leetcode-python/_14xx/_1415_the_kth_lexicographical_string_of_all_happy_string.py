import unittest
from typing import List


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []

        def backtrack(i: int, path: List[str]):
            if i == n:
                ans.append("".join(path))
                return False
            if len(ans) == k:
                return True
            for c in ('a', 'b', 'c'):
                if i > 0 and c == path[-1]:
                    continue
                path.append(c)
                if backtrack(i + 1, path):
                    return True
                path.pop()

        backtrack(0, [])
        if k > len(ans):
            return ""
        return ans[k-1]


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.getHappyString(n=1, k=3)
        self.assertEqual(actual, "c")

    def test_case_2(self):
        actual = self.s.getHappyString(n=1, k=4)
        self.assertEqual(actual, "")

    def test_case_3(self):
        actual = self.s.getHappyString(n=3, k=9)
        self.assertEqual(actual, "cab")

    def test_case_4(self):
        actual = self.s.getHappyString(n=2, k=5)
        self.assertEqual(actual, "ca")

    def test_case_5(self):
        actual = self.s.getHappyString(n=2, k=8)
        self.assertEqual(actual, "")


if __name__ == '__main__':
    unittest.main()
