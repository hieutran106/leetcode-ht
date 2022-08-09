package easy._392;

import org.junit.Assert;
import org.junit.Test;

public class SubsequenceStringTests {
    @Test
    public void testCase1() {
        var s = new Solution();
        var result = s.isSubsequence("abc", "ahbgdc");
        Assert.assertEquals(true, result);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var result = s.isSubsequence("axc", "ahbgdc");
        Assert.assertEquals(result, false);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var result = s.isSubsequence("", "ahbgdc");
        Assert.assertEquals(result, true);
    }
}
