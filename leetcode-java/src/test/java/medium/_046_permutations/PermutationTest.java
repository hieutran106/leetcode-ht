package medium._046_permutations;

import org.junit.Assert;
import org.junit.Test;

public class PermutationTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.permute(new int[]{1, 2, 3});
        Assert.assertEquals(actual.size(), 6);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.permute(new int[]{1, 2, 3, 4});
        Assert.assertEquals(actual.size(), 24);
    }
}
