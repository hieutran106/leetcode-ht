package medium._240;

import org.junit.Assert;
import org.junit.Test;

public class Search2DMatrixTest {
    @Test
    public void testCase1() {
        var input = new int[][] {
                {1,   4,  7, 11, 15},
                {2,   5,  8, 12, 19},
                {3,   6,  9, 16, 22},
                {10, 13, 14, 17, 24},
                {18, 21, 23, 26, 30}
        };
        var s = new Solution();
        var actual = s.searchMatrix(input, 5);
        Assert.assertEquals(actual, true);
    }

    @Test
    public void testCase2() {
        var input = new int[][] {
                {1,   4,  7, 11, 15},
                {2,   5,  8, 12, 19},
                {3,   6,  9, 16, 22},
                {10, 13, 14, 17, 24},
                {18, 21, 23, 26, 30}
        };
        var s = new Solution();
        var actual = s.searchMatrix(input, 20);
        Assert.assertEquals(actual, false);
    }

    @Test
    public void testCase3() {
        var input = new int[][]{{}};
        var s = new Solution();
        var actual = s.searchMatrix(input, 0);
        Assert.assertEquals(actual, false);
    }
}
