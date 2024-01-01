import unittest
from .solution import Solution
from typing import List
import heapq

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)

        res = 0
        min_heap = []
        for i in range(n):
            if i ==0 or colors[i] != colors[i-1]:
                # Create new min heap
                min_heap = []
                heapq.heapify(min_heap)
                heapq.heappush(min_heap, neededTime[i])
                continue
            heapq.heappush(min_heap, neededTime[i])
            if i == n -1 or colors[i] != colors[i+1]:
                total = 0
                while len(min_heap) > 1:
                    total = total + heapq.heappop(min_heap)

                res = res + total


        return res
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.minCost(colors = "abaac", neededTime = [1,2,3,4,5])
        self.assertEqual(3, actual)
        
    def test_case_2(self):
        actual = self.s.minCost(colors = "abc", neededTime = [1,2,3])
        self.assertEqual(0, actual)

    def test_case_3(self):
        actual = self.s.minCost(colors = "aabaa", neededTime = [1,2,3,4,1])
        self.assertEqual(2, actual)

    def test_case_4(self):
        actual = self.s.minCost(colors = "a", neededTime = [2])
        self.assertEqual(0, actual)

    def test_case_5(self):
        actual = self.s.minCost(colors = "aa", neededTime = [3,3])
        self.assertEqual(3, actual)

    def test_case_6(self):
        actual = self.s.minCost(colors = "bbbaaa", neededTime = [4,9,3,8,8,9])
        self.assertEqual(23, actual)

if __name__ == '__main__':
    unittest.main()

