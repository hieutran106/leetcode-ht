package easy._121_best_time_buy_sell_stock;

import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;

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
            let damage = weapon.damage * d20();
        }
    }

    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.maxProfit(new int[]{7, 1, 5, 3, 6, 4});
        Assert.assertEquals(5, actual);
    }

    @Test
    public void testCase0() {
        var s = new Solution();
        var actual = s.maxProfit(new int[]{7, 6, 4, 3, 1});
        Assert.assertEquals(0, actual);
    }
}