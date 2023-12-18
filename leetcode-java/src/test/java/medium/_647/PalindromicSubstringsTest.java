package medium._647;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class PalindromicSubstringsTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var result = s.countSubstrings("abc");
        assertEquals(3, result);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var result = s.countSubstrings("aaa");
        assertEquals(6, result);
    }
}
