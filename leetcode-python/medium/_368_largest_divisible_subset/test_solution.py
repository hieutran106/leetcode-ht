import unittest
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n  = len(nums)
        dp = [1] * len(nums)
        trace = [-1] * len(nums)
        for i in range(n):
            max_dp_val = 1
            max_dp_index = -1
            if i == 3:
                print("Test")
            for j in range(0, i):
                val = dp[j] + 1 if nums[i] % nums[j] == 0 else 1
                if val > max_dp_val:
                    max_dp_val = val
                    max_dp_index = j
            # assign
            dp[i] = max_dp_val
            trace[i] = max_dp_index

        print(nums)
        print(dp)
        print(trace)
        # find max in dp
        max_index = dp.index(max(dp))
        print("Max index:", max_index)
        res = []
        while True:
            res.append(nums[max_index])
            max_index = trace[max_index]
            if max_index == -1:
                break
        res.reverse()
        return res


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.largestDivisibleSubset(nums=[1, 2, 3])
        self.assertEqual(actual, [1, 2])

    def test_case_2(self):
        actual = self.s.largestDivisibleSubset(nums=[1, 2, 4, 8])
        self.assertEqual(actual, [1, 2, 4, 8])

    def test_case_3(self):
        actual = self.s.largestDivisibleSubset(nums=[3, 7, 8, 16, 32, 99])
        self.assertEqual(actual, [8, 16, 32])

    def test_case_4(self):
        actual = self.s.largestDivisibleSubset(nums=[3])
        self.assertEqual(actual, [3])

    def test_case_5(self):
        actual = self.s.largestDivisibleSubset(nums=[3, 17])
        self.assertEqual(actual, [3])

    def test_case_6(self):
        actual = self.s.largestDivisibleSubset(nums=[2, 3, 4, 8])
        self.assertEqual(actual, [2, 4, 8])

    def test_case_7(self):
        actual = self.s.largestDivisibleSubset(nums=[2, 3, 8, 9, 27])
        self.assertEqual(actual, [3, 9, 27])

    def test_case_8(self):
        actual = self.s.largestDivisibleSubset(nums=[2, 4, 6, 9, 19, 81, 729])
        self.assertEqual(actual, [9, 81, 729])

    def test_case_9(self):
        actual = self.s.largestDivisibleSubset(nums=[4,8,10,240])
        self.assertEqual(actual, [4, 8, 240])


if __name__ == '__main__':
    unittest.main()
