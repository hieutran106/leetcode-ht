import collections
import unittest
from typing import List

class Solution:
    def atMost(self, nums: List[int], k: int):
        # get the number of subarray that contains at most K distinct int
        # freq of number in the window
        count = collections.defaultdict(int)
        ans, l = 0, 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            while len(count) > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1
            # count the number of subarray ending at r that has at most k distinct integers
            print(f"At index {r=}, {l=}, found {r-l +1} match")
            ans += r - l + 1
        return ans

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # exact K = atMost(K) - atMost(k-1)
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

class Solution1:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def is_valid_window(c):
            return len(c) == k

        # hack test case
        s = set()
        for n in nums:
            s.add(n)
        if len(s) == 1:
            n = len(nums)
            return n * (n+1) /2

        count = collections.defaultdict(int)
        ans = 0
        l = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            extra = r
            if is_valid_window(count):
                while extra < len(nums) and nums[extra] in count:
                    extra += 1

            while is_valid_window(count):
                ans += extra - r
                print(f"At index {l=}, {extra=}, {r=}, found {extra - r} match")
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1
        return ans

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.subarraysWithKDistinct(nums = [1,2,1,2,3], k = 2)
        self.assertEqual(7, actual)
        
    def test_case_2(self):
        actual = self.s.subarraysWithKDistinct(nums = [1,2,1,3,4], k = 3)
        self.assertEqual(3, actual)

    def test_case_3(self):
        actual = self.s.subarraysWithKDistinct(nums = [1], k = 1)
        self.assertEqual(1, actual)


    def test_case_4(self):
        actual = self.s.subarraysWithKDistinct(nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], k = 1)
        self.assertEqual(435, actual)

    def test_case_5(self):
        actual = self.s.subarraysWithKDistinct(nums = [1,2,1,2,1,2,2,1,2,1,2,2,2,1,1,2,1,2,3], k = 2)
        self.assertEqual(149, actual)


    def test_case_6(self):
        atMost2 = self.s.atMost(nums = [1,2,1,2,3], k = 2)
        self.assertEqual(atMost2, 12)

if __name__ == '__main__':
    unittest.main()

