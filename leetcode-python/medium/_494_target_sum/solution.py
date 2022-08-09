from typing import List


# Transition function
# f(i, target) = f(i-1, target + nums[i]) + f(i-1, target - nums[i])
# Note:
#     Base case:
#         nums[0] == 0 and target == 0 ==> there are 2 ways
#         abs(t) == nums[0] ==> there are 1 ways
#         else ==> there are 0 ways

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dp(i, t) -> int:
            if i == 0:
                if nums[i] == 0 and t == 0:
                    return 2
                elif abs(t) == nums[0]:
                    return 1
                else:
                    return 0

            my_tuple = (i, t)
            if my_tuple in memo:
                return memo[my_tuple]
            result = dp(i - 1, t - nums[i]) + dp(i - 1, t + nums[i])
            memo[my_tuple] = result
            return result

        return dp(n - 1, target)
