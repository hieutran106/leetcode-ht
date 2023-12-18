package hard._051_n_queens;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class NQueensTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.solveNQueens(4);
        assertEquals(actual.size(), 2);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.solveNQueens(1);
        assertEquals(actual.size(), 1);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.solveNQueens(2);
        assertEquals(actual.size(), 0);
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        var actual = s.solveNQueens(8);
        assertEquals(actual.size(), 92);
    }
}
