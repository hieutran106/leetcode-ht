package easy._121_best_time_buy_sell_stock;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class SolutionTest {
    public static class Solution {
        public int maxProfit(int[] prices) {
            var n = prices.length;
            var dp = new int[n];
            int min_price = prices[0];
            for (int i = 1; i < n; i++) {
                min_price = Math.min(prices[i-1], min_price);
                dp[i] = prices[i] - min_price;

            }
            return dp[n-1];
        }
    }

}