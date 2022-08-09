package medium._090_subsets_2;

import org.junit.Assert;
import org.junit.Test;

public class Subsets2Test {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.subsetsWithDup(new int[]{1, 2, 2});
        Assert.assertEquals(6, actual.size());
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.subsetsWithDup(new int[]{1});
        Assert.assertEquals(2, actual.size());
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.subsetsWithDup(new int[]{1, 2});
        Assert.assertEquals(4, actual.size());
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        var actual = s.subsetsWithDup(new int[]{2, 2, 2});
        Assert.assertEquals(4, actual.size());
    }

    @Test
    public void testCase5() {
        var s = new Solution();
        var actual = s.subsetsWithDup(new int[]{2, 2});
        Assert.assertEquals(3, actual.size());
    }
}
