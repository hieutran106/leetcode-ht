package medium._994_rotting_oranges;

import org.junit.Assert;
import org.junit.Test;

public class RottingOrangesTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var input = new int[][]{{2,1,1}, {1,1,0}, {0, 1,1}};
        var actual = s.orangesRotting(input);
        Assert.assertEquals(4, actual);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var input = new int[][]{{2,1,1}, {0,1,1}, {1, 0,1}};
        var actual = s.orangesRotting(input);
        Assert.assertEquals(-1, actual);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var input = new int[][]{{0, 2}};
        var actual = s.orangesRotting(input);
        Assert.assertEquals(0, actual);
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        var input = new int[][]{{0, 2}, {2, 0}};
        var actual = s.orangesRotting(input);
        Assert.assertEquals(0, actual);
    }

    @Test
    public void testCase5() {
        var s = new Solution();
        var input = new int[][]{{1, 0}, {0, 2}};
        var actual = s.orangesRotting(input);
        Assert.assertEquals(-1, actual);
    }
}
