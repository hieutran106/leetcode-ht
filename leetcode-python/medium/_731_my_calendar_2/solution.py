import heapq
from typing import List, Tuple


class MyCalendarTwo:
    bookings: List[Tuple[int, int]]

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        self.bookings.append((start, end))

        sorted_books = sorted(self.bookings)
        booking_count = 0
        min_heap = []  # save (b_end)

        for current_start, current_end in sorted_books:
            booking_count += 1
            heapq.heappush(min_heap, current_end)
            while min_heap and min_heap[0] <= current_start:
                booking_count -= 1
                heapq.heappop(min_heap)

            if booking_count > 2:
                self.bookings.pop()
                return False
        return True
