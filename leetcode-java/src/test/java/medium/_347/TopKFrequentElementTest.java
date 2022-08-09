package medium._347;

import org.junit.Assert;
import org.junit.Test;

public class TopKFrequentElementTest {
    @Test
    public void testCase1() {
        var input = new int[] {1,1,1,2,2,3};
        var s = new Solution();
        var actual = s.topKFrequent(input, 2);
        Assert.assertArrayEquals(new int[]{1,2}, actual);
    }

    @Test
    public void testCase2() {
        var input = new int[] {1,1,1};
        var s = new Solution();
        var actual = s.topKFrequent(input, 1);
        Assert.assertArrayEquals(new int[]{1}, actual);
    }
}
