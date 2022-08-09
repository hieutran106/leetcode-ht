class Solution:
    def canPartition(self, nums) -> bool:
        n = len(nums)
        total = sum(nums)

        if n == 1 or total % 2 == 1:
            return False
        memo = [[None] * (total // 2 + 1) for _ in range(n - 1)]
        # base case
        for i in range(total // 2 + 1):
            memo[0][i] = False

        memo[0][0] = True
        if nums[0] <= total // 2:
            memo[0][nums[0]] = True

        # Going to the second last number is sufficient, thus n-2
        return self.dp(n - 2, total // 2, memo, nums)

    def dp(self, item_index, sum, memo, nums):
        if memo[item_index][sum] is not None:
            return memo[item_index][sum]

        # if we put the current number in
        use_curr_number = (
            self.dp(item_index - 1, sum - nums[item_index], memo, nums)
            if (sum - nums[item_index] >= 0)
            else False
        )
        res = use_curr_number or self.dp(item_index - 1, sum, memo, nums)
        memo[item_index][sum] = res
        return res
