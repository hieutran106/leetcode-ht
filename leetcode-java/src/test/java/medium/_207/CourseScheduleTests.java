package medium._207;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class CourseScheduleTests {
    @Test
    public void testCase1() {
        var solution = new Solution();
        int[][] pre = {{0,1}};
        var result = solution.canFinish(2, pre);
        assertEquals(result, true);
    }

    @Test
    public void testCase2() {
        var solution = new Solution();
        int[][] pre = {{1,0}, {0, 1}};
        var result = solution.canFinish(2, pre);
        assertEquals(false, result );
    }
    @Test
    public void testCase3() {
        var solution = new Solution();
        int[][] pre = {{1,0}, {2, 0}, {3, 1}, {3, 2}};
        var result = solution.canFinish(4, pre);
        assertEquals(true, result );
    }


}
