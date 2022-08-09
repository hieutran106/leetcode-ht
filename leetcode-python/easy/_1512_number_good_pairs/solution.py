# tags: math

from typing import List
import others

'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
'''


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    sum += 1

        return sum


'''
    Explanation: from n value ==> we have n *(n-1) /2 pairs
'''


class Solution2:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # number of occurrences for each value
        counter = others.Counter(nums).values()
        # number of pairs
        pairs = [n * (n - 1) / 2 for n in counter]
        return sum(pairs)
