package medium._332_coin_change;


import java.util.HashMap;

/**
 * Method: Dynamic programming
 */
public class Solution implements ISolution {
    public int change(int[] coins, int amount) {
        HashMap<Integer, Integer> map = new HashMap<>();
        return dp(coins, amount, map);
    }

    private int dp(int[] coins, int amount, HashMap<Integer, Integer> map) {
        if (amount ==0) {
            return 0;
        }
        if (amount < 0) {
            return -1;
        }
        // Check the memo to avoid double counting
        if (map.containsKey(amount)) {
            return map.get(amount);
        }
        int res = Integer.MAX_VALUE;
        for (var coin: coins) {
            int subproblem = dp(coins, amount - coin, map);
            if (subproblem == -1) {
                continue;
            }
            res = Math.min(res, subproblem + 1);
        }

        // note on memo
        map.put(amount, res != Integer.MAX_VALUE ? res : -1);
        return map.get(amount);
    }


}
