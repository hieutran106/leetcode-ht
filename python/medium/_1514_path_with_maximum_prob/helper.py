import heapq
from typing import List


class MaxHeap:
    """
    The easiest way is to invert the value of the keys and use heapq. For example, turn 1000.0 into -1000.0 and 5.0 into -5.0.
    """

    def __init__(self):
        self.data = []

    def push(self, item, cost):
        heapq.heappush(self.data, (-cost, item))

    def pop(self):
        (inverted_cost, item) = heapq.heappop(self.data)
        return item, -inverted_cost

    def is_empty(self):
        return len(self.data) == 0
