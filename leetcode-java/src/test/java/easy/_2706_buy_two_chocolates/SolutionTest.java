package easy._2706_buy_two_chocolates;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;

public class SolutionTest {
    public static class Solution {
        public int buyChoco(int[] prices, int money) {
            int minOne = Integer.MAX_VALUE;
            int minTwo = Integer.MAX_VALUE;
            for (int price: prices) {
                if (price < minOne) {
                    minTwo = minOne;
                    minOne = price;
                } else {
                    if (price < minTwo) {
                        minTwo = price;
                    }
                }
            }

            int leftOver = money - (minOne + minTwo);
            return leftOver >= 0 ? leftOver : money;
        }
    }

    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.buyChoco(new int[]{1,2,2}, 3);
        Assertions.assertEquals(actual, 0);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.buyChoco(new int[]{3,2,3}, 3);
        Assertions.assertEquals(actual, 3);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.buyChoco(new int[]{2,2}, 4);
        Assertions.assertEquals(actual, 0);
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        var actual = s.buyChoco(new int[]{4,5}, 10);
        Assertions.assertEquals(actual, 1);
    }
}