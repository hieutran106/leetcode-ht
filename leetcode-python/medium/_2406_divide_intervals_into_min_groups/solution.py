from typing import List
import heapq


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # init a min heap
        result = []
        # sort intervals by start_time and end_time
        intervals.sort()
        # always push the first interval into heap
        heapq.heappush(result, intervals[0][1])
        # checking the rest
        for left, right in intervals[1:]:
            if left > result[0]:
                # no overlapping, use existing group
                heapq.heappop(result)
            # in both case, always push right value to heap
            heapq.heappush(result, right)

        return len(result)
