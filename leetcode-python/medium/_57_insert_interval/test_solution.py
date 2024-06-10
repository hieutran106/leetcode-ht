import unittest
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # This solution operates in 3 phrases:
        #   1. Add all the intervals starting before newInterval to merged
        #   2. Merge all overlapping intervals with newInterval and add that merged interval to merged
        #   3. Add all the intervals starting after newInterval to merged
        merged = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        while i < n and (intervals[i][0] <= newInterval[1]):
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        merged.append(newInterval)

        for j in range(i, n):
            merged.append(intervals[j])
        return merged






class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5])
        self.assertEqual([[1, 5], [6, 9]], actual)

    def test_case_2(self):
        actual = self.s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8])
        self.assertEqual([[1, 2], [3, 10], [12, 16]], actual)

    def test_case_3(self):
        actual = self.s.insert(intervals=[], newInterval=[5, 7])
        self.assertEqual([[5, 7]], actual)

    def test_case_4(self):
        actual = self.s.insert(intervals=[[1, 5]], newInterval=[6, 8])
        self.assertEqual([[1, 5], [6, 8]], actual)


if __name__ == '__main__':
    unittest.main()
