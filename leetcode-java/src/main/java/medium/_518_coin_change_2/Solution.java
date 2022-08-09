package medium._518_coin_change_2;

// DP top-down
public class Solution implements ISolution {
    public int change(int amount, int[] coins)  {
        if (amount == 0) {
            return 1;
        }
        if (coins.length ==0) {
            return 0;
        }

        int[][] memo = new int[amount+1][coins.length];
        for (int i =0; i < memo.length; i++)
            for (int j =0; j < memo[0].length;j ++) {
                memo[i][j] = Integer.MAX_VALUE;
            }
        return dp(amount, coins, 0, memo);
    }

    private int dp(int amount, int[] coins, int k, int[][] memo) {
        if (amount == 0) {
            return 1;
        }
        if (k == coins.length) {
            return 0;
        }
        if (k == coins.length - 1) {
            return amount % coins[k] == 0 ? 1 : 0;
        }

        if (memo[amount][k] != Integer.MAX_VALUE) {
            return memo[amount][k];
        }

        int currCoin = coins[k];
        int numberMax = amount / currCoin;
        int way = 0;
        for (int i =0; i<=numberMax;i++) {
            var subproblem = dp(amount - currCoin * i, coins, k + 1, memo);
            way = way + subproblem;
        }
        memo[amount][k] = way;
        return memo[amount][k];
    }

}
