class Solution:
    def maxSubArray(self, nums) -> int:
        """
        Idea: Finding maximum subarray end at j (0 <=j <= n)
        Return: max(dp[i]) (0<=i<=n)
        :param nums:
        :return:
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])

        return max(dp)
