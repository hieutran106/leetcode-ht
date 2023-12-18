package medium._063;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class UniquePathsTest {
    @Test
    public void testCas1() {
        var s = new Solution();
        int[][] input = new int[][]{{0,0,0}, {0, 1, 0}, {0,0,0}};
        var result = s.uniquePathsWithObstacles(input);
        assertEquals(2, result);
    }

    @Test
    public void testCas4() {
        var s = new Solution();
        int[][] input = new int[][]{{0,0,0}, {0, 0, 0}, {0,0,0}};
        var result = s.uniquePathsWithObstacles(input);
        assertEquals(6, result);
    }

    @Test
    public void testCas2() {
        var s = new Solution();
        int[][] input = new int[][]{{1}};
        var result = s.uniquePathsWithObstacles(input);
        assertEquals(0, result);
    }

    @Test
    public void testCas3() {
        var s = new Solution();
        int[][] input = new int[][]{{1, 0}};
        var result = s.uniquePathsWithObstacles(input);
        assertEquals(0, result);
    }
}
