package medium._518_coin_change_2;

// dp - bottom up solution
public class Solution2 implements ISolution{
    public int change(int amount, int[] coins) {
        int n = coins.length;
        int[][] dp = new int[n + 1][amount + 1];
        for (int i = 0; i <= n; i++)
            dp[i][0] = 1; // have 1 way to change 0 amount
        for (int c = 1; c <= n; c++) {
            for (int a = 1; a <= amount; a++) {
                dp[c][a] = dp[c - 1][a]; // skip ith coin
                if (a >= coins[c - 1])
                    dp[c][a] += dp[c][a - coins[c - 1]]; // use ith coin
            }
        }

        return dp[n][amount];
    }

}
