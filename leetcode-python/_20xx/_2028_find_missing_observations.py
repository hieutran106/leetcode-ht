import unittest
from typing import List
from collections import Counter


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # math + greedy
        total = mean * (n + len(rolls)) - sum(rolls)
        if total < n or total > 6*n:
            return []
        base = total // n
        extra = total - base * n
        ans = []
        for i in range(n):
            if i < extra:
                ans.append(base + 1)
            else:
                ans.append(base)
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.missingRolls(rolls=[3, 2, 4, 3], mean=4, n=2)
        counter1 = Counter(actual)
        counter2 = Counter([6, 6])
        self.assertEqual(counter2, counter1)

    def test_case_2(self):
        actual = self.s.missingRolls(rolls=[1, 5, 6], mean=3, n=4)
        counter1 = Counter(actual)
        counter2 = Counter([2, 3, 2, 2])
        self.assertEqual(counter2, counter1)

    def test_case_3(self):
        actual = self.s.missingRolls(rolls=[1, 2, 3, 4], mean=6, n=4)
        counter1 = Counter(actual)
        counter2 = Counter([])
        self.assertEqual(counter2, counter1)


if __name__ == '__main__':
    unittest.main()
