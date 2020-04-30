package medium._1143;

import org.junit.Assert;
import org.junit.Test;

public class LongestCommonSubsequenceTests {
    @Test
    public void testCase1() {
        var s = new Solution();
        var result = s.longestCommonSubsequence("abcde", "ace");
        Assert.assertEquals(3, result);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var result = s.longestCommonSubsequence("abc", "def");
        Assert.assertEquals(0, result);
    }
}
