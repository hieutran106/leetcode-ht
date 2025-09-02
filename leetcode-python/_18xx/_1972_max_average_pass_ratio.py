import unittest
from typing import List
import heapq
# Date: 2025-02-09
# Problem: 1972 max_average_pass_ratio
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [] # min heap
        for p, t in classes:
            delta = (p+1)/(t+1) - p/t # potential gain if we add extra student to this class
            heapq.heappush(heap, (-delta, p, t))
        for i in range(extraStudents):
            _, p, t = heapq.heappop(heap)
            # greedy
            delta = (p+2)/(t+2) - (p+1)/(t+1)
            heapq.heappush(heap, (-delta, p+1, t + 1))
        return sum([p/total for _, p, total in heap])/len(classes)
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.maxAverageRatio(classes = [[1,2],[3,5],[2,2]], extraStudents = 2)
        self.assertAlmostEqual(actual, 0.78333, None, "", 10 ** -5)
        
    def test_case_2(self):
        actual = self.s.maxAverageRatio(classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4)
        self.assertAlmostEqual(actual, 0.53485, None, "", 10 ** -5)

    def test_case_3(self):
        actual = self.s.maxAverageRatio(classes = [[1,2],[3,5]], extraStudents = 1)
        self.assertAlmostEqual(actual, 0.6333333333333333, None, "", 10 ** -5)


if __name__ == '__main__':
    unittest.main()

