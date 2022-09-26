import heapq
from typing import List, Tuple
import copy
class MyCalendarTwo:
    bookings: List[Tuple[int, int]]

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        bookings = copy.deepcopy(self.bookings)
        bookings = list(filter(lambda b: b[1] >= start, bookings))
        bookings.append((start, end))
        bookings.sort(reverse=True)
        print(bookings)

        book_num = 0
        min_heap = [] # save (b_end)

        for i in range(start, end):
            while bookings and i >= bookings[-1][0]:
                b_start, b_end = bookings.pop()
                book_num += 1
                heapq.heappush(min_heap, b_end)

            while min_heap and min_heap[0] == i:
                book_num -= 1
                heapq.heappop(min_heap)
            if book_num > 2:
                return False

        # save booking
        self.bookings.append((start, end))
        return True
