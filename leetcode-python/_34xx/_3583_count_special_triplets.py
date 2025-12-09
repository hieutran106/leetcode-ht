import unittest
from typing import List
import collections
# Date: 2025-12-09
# Problem: 3583 count_special_triplets
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:

        MOD = 10 ** 9 + 7
        n = len(nums)
        counter = collections.defaultdict(int)
        # frequency dict to track how many times value * 2 appears before the value at the current index
        prevFreq = [0] * n
        for i, n in enumerate(nums):
            prevFreq[i] = counter[n*2]
            counter[n] += 1

        # frequency dict to track how many times value * 2 appears after the value at the current index
        nextFreq = [0] * len(nums)
        counter = collections.defaultdict(int)
        for i in range(len(nums)-1, -1, -1):
            n = nums[i]
            nextFreq[i] = counter[n*2]
            counter[n] += 1

        ans = 0
        for i in range(len(nums)):
            # for each index i, compute contribution to the answer using prevFreq and nextFreq
            ans = (ans + prevFreq[i] * nextFreq[i]) % MOD
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.specialTriplets(nums = [6,3,6])
        self.assertEqual(1, actual)
        
    def test_case_2(self):
        actual = self.s.specialTriplets(nums=[0,1,0,0])
        self.assertEqual(1, actual)

    def test_case_3(self):
        actual = self.s.specialTriplets(nums = [8,4,2,8,4])
        self.assertEqual(2, actual)

if __name__ == '__main__':
    unittest.main()

