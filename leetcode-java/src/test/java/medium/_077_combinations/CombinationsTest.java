package medium._077_combinations;

import org.junit.Assert;
import org.junit.Test;

public class CombinationsTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.combine(4, 2);
        Assert.assertEquals(actual.size(), 6);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.combine(1, 1);
        Assert.assertEquals(actual.size(), 1);
    }
}
