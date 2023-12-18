package medium._056;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import org.junit.jupiter.api.Test;

public class MergeIntervalsTest {
    @Test
    public void testCase1() {
        int[][] input = new int[][]{{1,3}, {2,6}, {8,10}, {15, 18}};
        var s= new Solution();
        var result = s.merge(input);
        assertArrayEquals(new int[][]{{1,6}, {8,10}, {15,18}}, result);
    }

    @Test
    public void testCase2() {
        int[][] input = new int[][]{{1,4}, {4,5}};
        var s= new Solution();
        var result = s.merge(input);
        assertArrayEquals(new int[][]{{1, 5}}, result);
    }

    @Test
    public void testCase4() {
        int[][] input = new int[][]{{1,4}};
        var s= new Solution();
        var result = s.merge(input);
        assertArrayEquals(new int[][]{{1, 4}}, result);
    }

    @Test
    public void testCase5() {
        int[][] input = new int[][]{{1,4}, {0, 4}};
        var s= new Solution();
        var result = s.merge(input);
        assertArrayEquals(new int[][]{{0, 4}}, result);
    }

    @Test
    public void testCase6() {
        int[][] input = new int[][]{{1,4}, {2, 3}};
        var s= new Solution();
        var result = s.merge(input);
        assertArrayEquals(new int[][]{{1, 4}}, result);
    }
}
