from math import isqrt


class Solution:
    """
    dp(n) = min([dp(i % ele) + (i//ele) for ele in squares if ele <= i])
    """
    def numSquares(self, n: int) -> int:
        # array of perfect square number that still smaller than n
        squares = [i * i for i in range(1, isqrt(n) + 1)]
        memo = {}

        def dp(i):
            if i == 0:
                return 0
            if i in memo:
                return memo[i]
            # transition function
            result = min([dp(i % ele) + (i // ele) for ele in squares if ele <= i])
            memo[i] = result
            return result

        return dp(n)
