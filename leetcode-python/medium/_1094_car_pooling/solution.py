from typing import List
import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda trip: trip[1], reverse=True)
        print(trips)
        min_heap = []  # (curr_to, c)
        total_capacity = 0
        curr_index = trips[-1][1]
        while min_heap or trips:
            while trips and trips[-1][1] == curr_index:
                # Pull trip into heap
                c, curr_from, curr_to = trips.pop()
                total_capacity += c
                heapq.heappush(min_heap, (curr_to, c))
            while min_heap and min_heap[0][0] <= curr_index:
                _, c = heapq.heappop(min_heap)
                total_capacity -= c
            if total_capacity > capacity:
                return False
            curr_index += 1
        return True
