from typing import List
import heapq


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """Use a min heap to keep track. Value of i-th step can be calculated based on
            - value of (i-1)th value
            and minus value pop from heap
            and plus value push to heap
        """
        buffer = [0] * (n + 1)
        bookings.sort(reverse=True)
        min_heap = []
        for i in range(1, n + 1):
            total_change = 0
            while min_heap and min_heap[0][0] < i:
                _, value = heapq.heappop(min_heap)
                total_change -= value

            while bookings and bookings[-1][0] == i:
                _, right, value = bookings.pop()
                heapq.heappush(min_heap, (right, value))
                total_change += value

            buffer[i] = buffer[i - 1] + total_change
        return buffer[1:]
