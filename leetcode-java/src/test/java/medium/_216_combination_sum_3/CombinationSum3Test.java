package medium._216_combination_sum_3;


import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class CombinationSum3Test {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.combinationSum3(3, 7);
        assertEquals(actual.size(), 1);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.combinationSum3(3, 9);
        assertEquals(actual.size(), 3);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.combinationSum3(3, 1);
        assertEquals(actual.size(), 0);
    }
}
