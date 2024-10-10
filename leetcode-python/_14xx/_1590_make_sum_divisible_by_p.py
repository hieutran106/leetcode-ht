import unittest
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0
        # in this problem, we need to find subarray such as its sum % p == target
        prefix_sum = [0]
        for n in nums:
            prefix_sum.append(n + prefix_sum[-1])
        # dict, key: remainder, value: index last time we saw it
        d = {}
        ans = float("inf")
        for i, v in enumerate(prefix_sum):
            curr_remainder = v % p
            expected_remainer = (curr_remainder - target) % p
            if expected_remainer < 0:
                expected_remainer = p + expected_remainer
            if expected_remainer in d:
                print(f"Found a subarray at current {i}, prev={d[expected_remainer]}")
                subarray_length = i - d[expected_remainer]
                ans = min(ans, subarray_length)
            d[curr_remainder] = i
        if ans == len(nums):
            return -1
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.minSubarray(nums=[3, 1, 4, 2], p=6)
        self.assertEqual(1, actual)

    def test_case_2(self):
        actual = self.s.minSubarray(nums=[6, 3, 5, 2], p=9)
        self.assertEqual(2, actual)

    def test_case_3(self):
        actual = self.s.minSubarray(nums=[1, 2, 3], p=3)
        self.assertEqual(0, actual)

    def test_case_4(self):
        actual = self.s.minSubarray(nums=[1, 5], p=4)
        self.assertEqual(-1, actual)

    def test_case_5(self):
        actual = self.s.minSubarray(nums=[1, 1, 1, 1, 5, 5, 10, 1, 2, 2], p=5)
        self.assertEqual(2, actual)


if __name__ == '__main__':
    unittest.main()
