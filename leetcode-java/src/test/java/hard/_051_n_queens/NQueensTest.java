package hard._051_n_queens;

import org.junit.Assert;
import org.junit.Test;

public class NQueensTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.solveNQueens(4);
        Assert.assertEquals(actual.size(), 2);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.solveNQueens(1);
        Assert.assertEquals(actual.size(), 1);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.solveNQueens(2);
        Assert.assertEquals(actual.size(), 0);
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        var actual = s.solveNQueens(8);
        Assert.assertEquals(actual.size(), 92);
    }
}
