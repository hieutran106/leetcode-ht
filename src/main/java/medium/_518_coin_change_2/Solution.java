package medium._518_coin_change_2;

public class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        // init value ?
        // base case
        dp[0] = 0;
        for (int i = 1; i < dp.length; i++) {

            for (int coin: coins) {
                var subproblem = i - coin;
                if (subproblem < 0) continue;
                dp[i] = dp[i] + dp[subproblem];
            }
        }

        return dp[amount];
    }
}
