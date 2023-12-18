package medium._518_coin_change_2;


import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class CoinChange2Test {

    public static ISolution getSolution() {
        return new Solution2();
    }

    @Test
    public void testCase1() {
        var s = CoinChange2Test.getSolution();
        var actual = s.change(5, new int[]{1, 2, 5});
        assertEquals(4, actual);
    }

    @Test
    public void testCase2() {
        var s = CoinChange2Test.getSolution();
        var actual = s.change(3, new int[]{2});
        assertEquals(0, actual);
    }

    @Test
    public void testCase3() {
        var s = CoinChange2Test.getSolution();
        var actual = s.change(3, new int[]{2});
        assertEquals(0, actual);
    }

    @Test
    public void testCase4() {
        var s = CoinChange2Test.getSolution();
        var actual = s.change(3, new int[]{2, 1});
        assertEquals(2, actual);
    }

    @Test
    public void testCase5() {
        var s = CoinChange2Test.getSolution();
        var actual = s.change(5, new int[]{});
        assertEquals(0, actual);
    }

    @Test
    public void testCase6() {
        var s = CoinChange2Test.getSolution();
        var actual = s.change(0, new int[]{});
        assertEquals(1, actual);
    }

    @Test
    public void testCase7() {
        var s = CoinChange2Test.getSolution();
        var actual = s.change(1000, new int[]{3, 5, 7, 8, 9, 10, 11});
        assertEquals(1952879228, actual);
    }


}
