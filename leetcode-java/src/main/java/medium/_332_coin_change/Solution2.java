package medium._332_coin_change;

/*
  DP bottom up solution
 */
public class Solution2 implements ISolution {

    public int change(int[] coins, int amount) {
        int[] dp = new int[amount+1];
        for (int i =0; i < dp.length; i++) {
            dp[i] = amount + 1;
        }

        // the array size is amount +1, and the initial value os also amount + 1
        // reason: the number of coins that can be added to "amount" can only be equal to amount at most
        //          when all one-dollar coin
        //          init value to amount + 1 is the same to infinity for subsequent minimization
        // base case
        dp[0] = 0;
        for (int i =0; i < dp.length; i++) {
            // the inner loop is finding the minimum of + 1 for all sub problems
            for (int coin: coins) {
                if (i - coin < 0) continue;
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
        return (dp[amount] == amount + 1) ? -1 : dp[amount];

    }
}
