from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] != 0:
                continue
            # swap between zero and the first non-zero element
            j = i + 1
            while (j < len(nums)):
                if nums[j] != 0:
                    # swap
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    break
                j += 1

        return nums

