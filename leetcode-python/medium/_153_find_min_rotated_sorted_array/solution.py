from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            num_l = nums[l]
            num_r = nums[r]
            num_m = nums[mid]
            if num_l < num_m and num_m > num_r:
                # search right side
                l = mid + 1
            elif num_l > num_m and num_m < num_r:
                # search left
                r = mid
            elif num_l >= num_m > num_r:
                return num_r
            else:
                return num_l
        return nums[l]
