package medium._300_longest_increasing_subsequence;

import org.junit.Assert;
import org.junit.Test;

public class TestLongestIncSubsequence {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.lengthOfLIS(new int[]{10,9,2,5,3,7,101,18});
        Assert.assertEquals(4, actual);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.lengthOfLIS(new int[]{1});
        Assert.assertEquals(1, actual);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.lengthOfLIS(new int[]{10, 2, 3,4});
        Assert.assertEquals(3, actual);
    }
}

