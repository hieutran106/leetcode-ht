package easy._198_house_robber;

import org.junit.Assert;
import org.junit.Test;

public class HouseRobberTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.rob(new int[]{1, 2, 3, 1});
        Assert.assertEquals(4, actual);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.rob(new int[]{2,7,9,3,1});
        Assert.assertEquals(12, actual);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.rob(new int[]{7, 2, 1, 15});
        Assert.assertEquals(22, actual);
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        var actual = s.rob(new int[]{1, 2, 1, 2, 4});
        Assert.assertEquals(6, actual);
    }

    @Test
    public void testCase5() {
        var s = new Solution();
        var actual = s.rob(new int[]{1});
        Assert.assertEquals(1, actual);
    }

    @Test
    public void testCase6() {
        var s = new Solution();
        var actual = s.rob(new int[]{0, 1});
        Assert.assertEquals(1, actual);
    }
}
