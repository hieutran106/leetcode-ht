from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        while nums:
            first = nums.pop()
            last = first + 1
            # increase
            while last in nums:
                nums.remove(last)
                last += 1
            while first - 1 in nums:
                nums.remove(first-1)
                first = first - 1

            if (last - first) > longest:
                longest = last - first
        return longest


