import unittest
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS(i) is the length of the LIS ending at index i such that
        # nums[i] is the last element of the LIS
        # Complexity: O(n^2)
        LIS = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        print(LIS)
        return max(LIS)


class BruteForceSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        1. Generate all possible subsequences of the input array
        2. Check if each subsequence is increasing
        3. Keep track of the longest increasing subsequence found
        """

        def generate_subsequences(nums: List[int]):
            all_subsequences = []

            def backtrack(i: int, curr: List[int]):
                if i == len(nums):
                    all_subsequences.append(curr[:])
                    return
                # Include i-th num
                curr.append(nums[i])
                backtrack(i + 1, curr)
                # Do not include i-th num
                curr.pop()
                backtrack(i + 1, curr)

            backtrack(0, [])
            return all_subsequences

        def is_increasing(nums: List[int]):
            for i in range(1, len(nums)):
                if nums[i] <= nums[i - 1]:
                    return False
            return True

        ans = 0
        all_subsequences = generate_subsequences(nums)
        for sub in all_subsequences:
            if is_increasing(sub):
                ans = max(ans, len(sub))
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
        # self.s = BruteForceSolution()

    def test_case_1(self):
        actual = self.s.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18])
        self.assertEqual(4, actual)

    def test_case_2(self):
        actual = self.s.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3])
        self.assertEqual(4, actual)

    def test_case_3(self):
        actual = self.s.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7])
        self.assertEqual(1, actual)


if __name__ == '__main__':
    unittest.main()
