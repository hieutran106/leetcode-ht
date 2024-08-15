import unittest
from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(nums)


    def add(self, val: int) -> int:
        heapq.heappush(self.nums , val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

class MyTestCase(unittest.TestCase):
    
    def test_case_1(self):
        kclass = KthLargest(3, [4, 5, 8, 2])

        self.assertEqual(4, kclass.add(3))
        self.assertEqual(5, kclass.add(5))
        self.assertEqual(5, kclass.add(10))
        
    def test_case_2(self):
        pass

if __name__ == '__main__':
    unittest.main()

