import unittest
from typing import List
import heapq
# Date: 2025-18-07
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # Divide the nums into 2 parts, then
        # find the k smallest numbers in the first half, and k the largest numbers in the second half
        k = len(nums) // 3

        max_heap = [] # to find the k smallest number, we use a max heap
        k_smallest = []
        curr_sum = 0 # to optimize, curr_sum = -sum(max_heap))
        for n in nums:
            if len(max_heap) < k:
                heapq.heappush(max_heap, -n)
                curr_sum += n
            else:
                top = max_heap[0]
                if n < -top:
                    heapq.heapreplace(max_heap, -n)
                    curr_sum += n + top
            k_smallest.append(curr_sum)

        min_heap = [] # to find the k largest numbers, we use a min heap
        k_largest = []
        curr_sum = 0
        for n in reversed(nums):
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
                curr_sum += n
            else:
                top = min_heap[0]
                if n > top:
                    heapq.heapreplace(min_heap, n)
                    curr_sum += n - top

            k_largest.append(curr_sum)

        k_largest.reverse()

        ans = float("inf")
        for i in range(k-1, len(nums) - k):
            ans = min(ans, k_smallest[i] - k_largest[i+1])
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.minimumDifference(nums = [3,1,2])
        self.assertEqual(-1, actual)
        
    def test_case_2(self):
        actual = self.s.minimumDifference(nums = [7,9,5,8,1,3])
        self.assertEqual(1, actual)

if __name__ == '__main__':
    unittest.main()

