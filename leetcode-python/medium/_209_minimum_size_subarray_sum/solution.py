from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        sum_window = nums[0]
        min_range = 10e5 + 1
        while right < n:
            if sum_window < target:
                # print("Enlarge window, by change right pointer")
                right += 1
                if right < n:
                    sum_window += nums[right]
            else:
                min_range = min(min_range, right - left + 1)
                # print(f"Found range: {min_range=} at {right=} and {left=}")
                sum_window -= nums[left]
                left += 1
        return min_range if min_range != 10e5 +1 else 0

