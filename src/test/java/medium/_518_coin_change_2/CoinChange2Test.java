package medium._518_coin_change_2;

import org.junit.Assert;
import org.junit.Test;

public class CoinChange2Test {

    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.change(5, new int[]{1, 2, 5});
        Assert.assertEquals(4, actual);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.change(3, new int[]{2});
        Assert.assertEquals(0, actual);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.change(3, new int[]{2});
        Assert.assertEquals(0, actual);
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        var actual = s.change(3, new int[]{1, 2});
        Assert.assertEquals(2, actual);
    }
}
