from typing import List


class NumArray:
    prefix_sum: List[int]

    def __init__(self, nums: List[int]):
        n = len(nums)
        prefix_sum = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        self.prefix_sum = prefix_sum

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
