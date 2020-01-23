package medium._215;

import org.junit.Assert;
import org.junit.Test;

public class KthLargestElementTest {
    @Test
    public void testCase1() {
        var solution = new KthLargestElement();
        var input = new int[]{3,2,1,5,6,4};
        var result = solution.findKthLargest(input, 2);
        Assert.assertEquals(result, 5);

    }

    @Test
    public void testCase2() {
        var solution = new KthLargestElement();
        var input = new int[]{3,2,3,1,2,4,5,5,6};
        var result = solution.findKthLargest(input, 4);
        Assert.assertEquals(4, result);
    }

}
