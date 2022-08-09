# tags: binary search
from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        left = 0
        right = sorted_nums[-1] - sorted_nums[0] + 1

        while left < right:
            mid = left + (right - left) // 2
            if self.is_feasible(sorted_nums, k, mid):
                left = mid + 1
            else:
                right = mid

        return left - 1

    def is_feasible(self, sorted_nums, k, value):
        def count_less_than(nums, start, target: int):
            left = start + 1
            right = len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left - start - 1

        count = 0
        for i in range(len(sorted_nums) - 1):
            target = sorted_nums[i] + value
            count += count_less_than(sorted_nums, i, target)
            if count >= k:
                return False

        return count < k


