package medium._078_subsets;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SubsetsTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.subsets(new int[]{1, 2, 3});
        assertEquals(actual.size(), 8);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.subsets(new int[]{1});
        assertEquals(actual.size(), 2);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.subsets(new int[]{1, 2});
        assertEquals(actual.size(), 4);
    }
}
