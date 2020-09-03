package medium._078_subsets;

import org.junit.Assert;
import org.junit.Test;

public class SubsetsTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.subsets(new int[]{1, 2, 3});
        Assert.assertEquals(actual.size(), 8);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.subsets(new int[]{1});
        Assert.assertEquals(actual.size(), 2);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.subsets(new int[]{1, 2});
        Assert.assertEquals(actual.size(), 4);
    }
}
