from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = left + (right - left) // 2
            if self.is_feasible(nums, m, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def is_feasible(self, nums: List[int], m: int, largest_sum: int) -> bool:
        """
        Is it feasible to divide array nums into m subarray with threshold being largest sum among those subarray
        :param nums:
        :param m:
        :param largest_sum:
        :return:
        """
        cuts = 0
        total = 0
        for num in nums:
            total += num
            if num > largest_sum:
                return False
            if total > largest_sum:
                cuts += 1
                total = num
        subarray_count = cuts + 1
        return subarray_count <= m
