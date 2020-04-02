package medium._207;

import org.junit.Assert;
import org.junit.Test;

public class CourseScheduleTests {
    @Test
    public void testCase1() {
        var solution = new Solution();
        int[][] pre = {{0,1}};
        var result = solution.canFinish(2, pre);
        Assert.assertEquals(result, true);
    }

    @Test
    public void testCase2() {
        var solution = new Solution();
        int[][] pre = {{1,0}, {0, 1}};
        var result = solution.canFinish(2, pre);
        Assert.assertEquals(false, result );
    }
    @Test
    public void testCase3() {
        var solution = new Solution();
        int[][] pre = {{1,0}, {2, 0}, {3, 1}, {3, 2}};
        var result = solution.canFinish(4, pre);
        Assert.assertEquals(true, result );
    }


}
