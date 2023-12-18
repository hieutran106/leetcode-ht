package medium._807_max_increase_to_keep_city_skyline;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;


public class SolutionTest {

    @Test
    public void testCase1() {
        Solution s = new Solution();
        int[][] input = new int[][]{
                {3,0,8,4},
                {2,4,5,7},
                {9,2,6,3},
                {0,3,1,0}
        };
        int output = s.maxIncreaseKeepingSkyline(input);
        assertEquals(35, output);
    }

    @Test
    public void testCase2() {
        Solution s = new Solution();
        int[][] input = new int[][]{
                {0,0,0},
                {0,0,0},
                {0,0,0}
        };
        int output = s.maxIncreaseKeepingSkyline(input);
        assertEquals(0, output);
    }

    @Test
    public void testCase3() {
        Solution s = new Solution();
        int[][] input = new int[][]{
                {0,0},
                {0,1}
        };
        int output = s.maxIncreaseKeepingSkyline(input);
        assertEquals(0, output);
    }
}