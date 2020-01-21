package medium._064;

import org.junit.Assert;
import org.junit.Test;

public class MinimumPathSumTests {

    @Test
    public  void testCase1() {
        int[][] input = {
                {1,3,1},
                {1,5,1},
                {4,2,1}
        };
        var solution = new MinimumPathSum();
        var result = solution.minPathSum(input);
        Assert.assertEquals(7, result);
    }

    @Test
    public void testCase2() {
        int[][] input = {
                {1,2,5},
                {3,2,1},

        };
        var solution = new MinimumPathSum();
        var result = solution.minPathSum(input);
        Assert.assertEquals(6, result);
    }

    @Test
    public void testCase3() {

    }
}
