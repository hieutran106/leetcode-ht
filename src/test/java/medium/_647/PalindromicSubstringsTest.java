package medium._647;

import org.junit.Assert;
import org.junit.Test;

public class PalindromicSubstringsTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var result = s.countSubstrings("abc");
        Assert.assertEquals(3, result);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var result = s.countSubstrings("aaa");
        Assert.assertEquals(6, result);
    }
}
