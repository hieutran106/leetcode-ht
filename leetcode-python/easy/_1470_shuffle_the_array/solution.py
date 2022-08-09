from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [None] * len(nums)
        for i in range(len(result)):
            half = i // 2
            if i %2 == 0:
                result[i] = nums[half]
            else:
                result[i] = nums[n + half]

        return result