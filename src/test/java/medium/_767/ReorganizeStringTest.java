package medium._767;

import org.junit.Assert;
import org.junit.Test;

public class ReorganizeStringTest {
    @Test
    public void testCase1() {
        var input = "aab";
        var s = new Solution();
        var actual = s.reorganizeString(input);
        Assert.assertEquals("aba", actual);
    }

    @Test
    public void testCase2() {
        var input = "aaab";
        var s = new Solution();
        var actual = s.reorganizeString(input);
        Assert.assertEquals("", actual);
    }

    @Test
    public void testCase3() {
        var input = "aaabbc";
        var s = new Solution();
        var actual = s.reorganizeString(input);
        Assert.assertEquals("ababac", actual);
    }
}
