import unittest
from .solution import Solution
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] = counter[num] + 1
            else:
                counter[num] = 1

        pairs = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        rows = [[] for _ in range(pairs[0][1])]
        for num, occ in pairs:
            for i in range(occ):
                rows[i].append(num)
        return rows


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.findMatrix(nums=[1, 3, 4, 1, 2, 3, 1])
        self.assertEqual([[1, 3, 4, 2], [1, 3], [1]], actual)

    def test_case_2(self):
        actual = self.s.findMatrix(nums=[1, 2, 3, 4])
        self.assertEqual([[1, 2, 3, 4]], actual)

    def test_case_3(self):
        actual = self.s.findMatrix(nums=[1, 1])
        self.assertEqual([[1], [1]], actual)

    def test_case_4(self):
        actual = self.s.findMatrix(nums=[2, 2, 3, 3, 3])
        self.assertEqual([[3, 2], [3, 2], [3]], actual)


if __name__ == '__main__':
    unittest.main()
