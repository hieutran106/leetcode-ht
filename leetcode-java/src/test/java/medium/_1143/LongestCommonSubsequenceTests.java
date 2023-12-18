package medium._1143;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class LongestCommonSubsequenceTests {
    @Test
    public void testCase1() {
        var s = new Solution();
        var result = s.longestCommonSubsequence("abcde", "ace");
        assertEquals(3, result);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var result = s.longestCommonSubsequence("abc", "def");
        assertEquals(0, result);
    }
}
