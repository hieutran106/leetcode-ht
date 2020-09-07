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
}
