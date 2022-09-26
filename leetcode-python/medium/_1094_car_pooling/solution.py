from typing import List
import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda trip: (trip[1], trip[2]))
        # print(trips)
        min_heap = []  # store (end, c)
        curr_capacity = 0
        for c, start, end in trips:
            curr_capacity += c
            heapq.heappush(min_heap, (end, c))

            while min_heap and min_heap[0][0] <= start:
                _, capacity_out = heapq.heappop(min_heap)
                curr_capacity -= capacity_out
            if curr_capacity > capacity:
                return False
        return True
