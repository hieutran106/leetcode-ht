package medium._077_combinations;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class CombinationsTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.combine(4, 2);
        assertEquals(actual.size(), 6);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.combine(1, 1);
        assertEquals(actual.size(), 1);
    }
}
