package easy._392;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SubsequenceStringTests {
    @Test
    public void testCase1() {
        var s = new Solution();
        var result = s.isSubsequence("abc", "ahbgdc");
        assertEquals(true, result);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var result = s.isSubsequence("axc", "ahbgdc");
        assertEquals(result, false);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var result = s.isSubsequence("", "ahbgdc");
        assertEquals(result, true);
    }
}
