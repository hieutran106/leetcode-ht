package medium._046_permutations;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class PermutationTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.permute(new int[]{1, 2, 3});
        assertEquals(actual.size(), 6);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.permute(new int[]{1, 2, 3, 4});
        assertEquals(actual.size(), 24);
    }
}
