from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        start = 0
        end = start + 1

        lengths = []
        while end < len(nums):
            if nums[end] > nums[end -1]:
                end += 1
            else:
                lengths.append(end - start)
                start = end
                end = start + 1

        lengths.append(end - start)
        return max(lengths)
