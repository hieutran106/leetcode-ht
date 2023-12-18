package medium._542;

//import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class MatrixTest {
    @Test
    public void testCase1() {
        int[][] intput = new int[][]{{0,0,0}, {0,1,0}, {1,1,1}};
        var s = new Solution();
        var result = s.updateMatrix(intput);
//        assertArrayEquals(new int[]{0,0,0}, result[0]);
        assertArrayEquals(new int[]{0,0,0}, result[0]);
        assertArrayEquals(new int[]{0,1,0}, result[1]);
        assertArrayEquals(new int[]{1,2,1}, result[2]);
    }

    @Test
    public void testCase2() {
        int[][] intput = new int[][]{{0,0,0}, {0,1,0}, {0,0,0}};
        var s = new Solution();
        var result = s.updateMatrix(intput);
        assertArrayEquals(new int[]{0,0,0}, result[0]);
        assertArrayEquals(new int[]{0,1,0}, result[1]);
        assertArrayEquals(new int[]{0,0,0}, result[2]);
    }

    @Test
    public void testCase3() {
        int[][] intput = new int[][]{{1,1,0}};
        var s = new Solution();
        var result = s.updateMatrix(intput);
        assertArrayEquals(new int[]{2,1,0}, result[0]);
    }

    @Test
    public void testCase4() {
        int[][] intput = new int[][]{{0}};
        var s = new Solution();
        var result = s.updateMatrix(intput);
        assertArrayEquals(new int[]{0}, result[0]);
    }

    @Test
    public void testCase5() {
        int[][] intput = new int[][]{{0},{1}};
        var s = new Solution();
        var result = s.updateMatrix(intput);
        assertArrayEquals(new int[]{0}, result[0]);
        assertArrayEquals(new int[]{1}, result[1]);
    }

    @Test
    public void testCase6() {
        int[][] intput = new int[][]{{0},{1},{1},{1}};
        var s = new Solution();
        var result = s.updateMatrix(intput);
        assertArrayEquals(new int[]{0}, result[0]);
        assertArrayEquals(new int[]{1}, result[1]);
        assertArrayEquals(new int[]{2}, result[2]);
        assertArrayEquals(new int[]{3}, result[3]);
    }

    @Test
    public void testCase7() {
        int[][] intput = new int[][]{{0},{1},{1},{1}, {1}};
        var s = new Solution();
        var result = s.updateMatrix(intput);
        assertArrayEquals(new int[]{0}, result[0]);
        assertArrayEquals(new int[]{1}, result[1]);
        assertArrayEquals(new int[]{2}, result[2]);
        assertArrayEquals(new int[]{3}, result[3]);
        assertArrayEquals(new int[]{4}, result[4]);
    }

    @Test
    public void testCase8() {
        int[][] intput = new int[][]{{0, 1, 1, 1, 1}};
        var s = new Solution();
        var result = s.updateMatrix(intput);
        assertArrayEquals(new int[]{0, 1, 2, 3, 4}, result[0]);
    }
}
