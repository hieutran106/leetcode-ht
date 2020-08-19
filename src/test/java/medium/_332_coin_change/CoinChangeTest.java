package medium._332_coin_change;

import org.junit.Assert;
import org.junit.Test;

public class CoinChangeTest {
    public static ISolution getSolution() {
        return new Solution2();
    }

    @Test
    public void testCase1() {
        var s = CoinChangeTest.getSolution();
        var actual = s.change(new int[]{1, 2, 5}, 11);
        Assert.assertEquals(3, actual);
    }


    @Test
    public void testCase2() {
        var s = CoinChangeTest.getSolution();
        var actual = s.change(new int[]{2}, 3);
        Assert.assertEquals(-1, actual);
    }


    @Test
    public void testCase3() {
        var s = CoinChangeTest.getSolution();
        var actual = s.change(new int[]{1, 2, 5}, 3);
        Assert.assertEquals(actual, 2);
    }

    @Test
    public void testCase4() {
        var s = CoinChangeTest.getSolution();
        var actual = s.change(new int[]{1, 2, 5}, 4);
        Assert.assertEquals(actual, 2);
    }

    @Test
    public void testCase5() {
        var s = CoinChangeTest.getSolution();
        var actual = s.change(new int[]{1, 2, 5}, 2);
        Assert.assertEquals(actual, 1);
    }

    @Test
    public void testCase6() {
        var s = CoinChangeTest.getSolution();
        var actual = s.change(new int[]{1, 2}, 2);
        Assert.assertEquals(actual, 1);
    }

    @Test
    public void testCase7() {
        var s = CoinChangeTest.getSolution();
        var actual = s.change(new int[]{1, 2}, 3);
        Assert.assertEquals(actual, 2);
    }

    @Test
    public void testCase8() {
        var s = CoinChangeTest.getSolution();
        var actual = s.change(new int[]{1, 2, 5}, 3);
        Assert.assertEquals(actual, 2);
    }

    @Test
    public void testCase9() {
        var s = CoinChangeTest.getSolution();
        var actual = s.change(new int[]{2}, 1);
        Assert.assertEquals(-1, actual);
    }

    @Test
    public void testCase10() {
        var s = CoinChangeTest.getSolution();
        var actual = s.change(new int[]{1}, 0);
        Assert.assertEquals(0, actual);
    }

    @Test
    public void testCase11() {
        var s = CoinChangeTest.getSolution();
        var actual = s.change(new int[]{186, 419, 83, 408}, 2083);
        Assert.assertEquals(17, actual);
    }


    @Test
    public void testCase13() {
        var s = CoinChangeTest.getSolution();
        var actual = s.change(new int[]{11}, 6249);
        Assert.assertEquals(-1, actual);
    }

}
