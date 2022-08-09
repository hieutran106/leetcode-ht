from typing import List


def is_overlapped(i1, i2):
    return i1[1] >= i2[0]

class Solution:
    def findMinArrowShots(self, intervals: List[List[int]]) -> int:
        # inplace sort
        intervals.sort(key=lambda ele: ele[0])
        count = 0
        min_interval = intervals[0]
        for i in range(1, len(intervals)):
            if not is_overlapped(min_interval, intervals[i]):
                min_interval = intervals[i]
                continue

            # if there is overlap, keep interval that has smaller end time
            count += 1
            if intervals[i][1] < min_interval[1]:
                min_interval = intervals[i]
        return len(intervals) - count