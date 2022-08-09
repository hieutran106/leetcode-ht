from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Subproblem: memo[i] - length of LIS ending at i
        Solve original problem: max(memo)
        :param nums:
        :return:
        """
        n = len(nums)
        memo = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    memo[i] = max(memo[i], 1 + memo[j])

        return max(memo)




