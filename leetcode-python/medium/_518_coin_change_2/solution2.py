from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dp(i, target):
            if target == 0:
                return 1
            elif i == 0 and target != 0:
                return 0

            if (i, target) in memo:
                return memo[(i, target)]
            result = 0
            coin_num = target // coins[i - 1]
            for j in range(0, coin_num + 1):
                result = result + dp(i - 1, target - j * coins[i - 1])
            memo[(i, target)] = result
            return result

        return dp(len(coins), amount)
