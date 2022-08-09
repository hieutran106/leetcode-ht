package easy._167;

import org.junit.Assert;
import org.junit.Test;

public class TwoSum2Test {
    @Test
    public void testCase1() {
        var input = new int[]{2,7,11,15};
        int target = 9;
        var s= new Solution();
        var actuals = s.twoSum(input, target);
        Assert.assertArrayEquals(new int[]{1,2}, actuals);
    }

    @Test
    public void testCase2() {
        var input = new int[]{2,3,4,5,6,7,9,10,15};
        int target = 18;
        var s= new Solution();
        var actuals = s.twoSum(input, target);
        Assert.assertArrayEquals(new int[]{2,9}, actuals);
    }

    @Test
    public void testCase3() {
        var input = new int[]{2,3,4,5};
        int target = 8;
        var s= new Solution();
        var actuals = s.twoSum(input, target);
        Assert.assertArrayEquals(new int[]{2,4}, actuals);
    }

    @Test
    public void testCase4() {
        var input = new int[]{2,3,4,5,6,7,9,10,15};
        int target = 18;
        var s= new Solution2_TwoPointer();
        var actuals = s.twoSum(input, target);
        Assert.assertArrayEquals(new int[]{2,9}, actuals);
    }

    @Test
    public void testCase5() {
        var input = new int[]{2,3,4,5};
        int target = 8;
        var s= new Solution2_TwoPointer();
        var actuals = s.twoSum(input, target);
        Assert.assertArrayEquals(new int[]{2,4}, actuals);

    }
}
