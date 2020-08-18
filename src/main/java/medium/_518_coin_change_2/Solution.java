package medium._518_coin_change_2;

import java.util.Arrays;

public class Solution {
    public int change(int amount, int[] coins) {
        if (amount < 0) {
            return 0;
        }
        // base case
        if (coins.length ==0) {
           return amount == 0 ? 1 : 0;
        }
        if (coins.length == 1) {
            return amount % coins[0] == 0 ? 1: 0;
        }
        int coinMax = coins[0];
        int numberMax = amount / coinMax;
        int way = 0;
        int[] subCoins = Arrays.copyOfRange(coins, 1, coins.length);
        for (int i = 0; i <= numberMax; i++) {
            var subproblem = change(amount - coinMax*i, subCoins);
            way = way + subproblem;
        }
        return way;
    }
}
