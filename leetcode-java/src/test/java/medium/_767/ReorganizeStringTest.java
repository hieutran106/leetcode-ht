package medium._767;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class ReorganizeStringTest {
    @Test
    public void testCase1() {
        var input = "aab";
        var s = new Solution();
        var actual = s.reorganizeString(input);
        assertEquals("aba", actual);
    }

    @Test
    public void testCase2() {
        var input = "aaab";
        var s = new Solution();
        var actual = s.reorganizeString(input);
        assertEquals("", actual);
    }

    @Test
    public void testCase3() {
        var input = "aaabbc";
        var s = new Solution();
        var actual = s.reorganizeString(input);
        assertEquals("ababac", actual);
    }
}
