import unittest
from typing import List
import collections
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Maintain a min heap of size k that contains the k largest elements seen
        Processing: For each remaining element in the array:
                    Compare it with the root (smallest element) of the min heap.
                    If the current element is larger, remove the root and insert the new element.
                    If it's smaller, ignore it and move to the next element.
        TC: O(nlogk) better than O(nlogn - if we just sort)
        """
        min_heap = []
        for n in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
                continue
            if len(min_heap) ==k and n > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, n)

        return heapq.heappop(min_heap)
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.findKthLargest(nums = [3,2,1,5,6,4], k = 2)
        self.assertEqual(5, actual)
        
    def test_case_2(self):
        actual = self.s.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4)
        self.assertEqual(4, actual)

    def test_case_3(self):
        actual = self.s.findKthLargest(nums = [1], k = 1)
        self.assertEqual(1, actual)

if __name__ == '__main__':
    unittest.main()

