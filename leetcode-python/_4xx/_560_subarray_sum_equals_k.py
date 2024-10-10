import unittest
from typing import List
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=[nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[-1])
        # dictionary - key: prefix sum, value: the number of time we have seen it
        d = collections.defaultdict(int)
        d[0] = 1
        ans = 0
        for v in prefix_sum:
            # we saw prefix sum v-k a number of time before, and at current index we have prefix sum v
            # it means that we found subarray sum equal k
            if d[v-k]:
                ans += d[v-k]
            d[v] += 1
        return ans




class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.subarraySum(nums = [1,1,1], k = 2)
        self.assertEqual(2, actual)
        
    def test_case_2(self):
        actual = self.s.subarraySum(nums = [1,2,3], k = 3)
        self.assertEqual(2, actual)

if __name__ == '__main__':
    unittest.main()

