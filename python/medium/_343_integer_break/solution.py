# tags: dp

'''
To find the max product of 8, break up 8 into the sum of two terms (keep the first term less than or equal to the second to prevent redundancy):

1 + 7 --> 1 * 7 = 7
2 + 6 --> 2 * 6 = 12
3 + 5 --> 3 * 5 = 15
4 + 4 --> 4 * 4 = 16
From this is seems that the max product 16, however we neglected to also break up each of the two terms into more terms, and check all those. Let's break the 6 into 3 + 3:

2 + 6 = 2 + 3 + 3 --> 2 * 3 * 3 = 18
which ends up being the correct answer. But another way to get this is to reuse the previously computed max product of 6, which we know to be 9:

2 * (3 * 3) = 2 * max_product_of_6 = 2 * 9 = 18
'''
class Solution:
    def integerBreak2(self, n: int) -> int:
        dp = [None for _ in range(n+1)]
        # base case
        dp[1] = 1
        dp[2] = 1

        for m in range(3, n+1):
            middle = 1 + m //2
            max_product = 0
            for i in range(1, middle + 1):
                # because i and m-i are breakable
                # need to check max(i, dp[i])
                product = max(i, dp[i]) * max(m-i, dp[m-i])
                max_product = max(max_product, product)

            dp[m] = max_product

        return dp[n]








