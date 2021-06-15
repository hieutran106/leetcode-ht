from typing import List
from utils.heap.maxheap import MaxHeap

import collections
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        Point = collections.namedtuple('Point', 'coordinate distance')
        points = [Point(p, -sqrt(p[0]**2 + p[1]**2)) for p in points]
        max_heap = MaxHeap(points, key=lambda x: x.distance)

        result = []
        for i in range(k):
            point = max_heap.remove()
            result.append(point.coordinate)

        return result
