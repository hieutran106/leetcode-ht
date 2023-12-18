package easy._190_reverse_bits;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class SolutionTest {

    @Test
    public void testCase1() {
        Solution s = new Solution();
        int actual = s.reverseBits(43261596 );
        assertEquals(actual, 964176192);
    }

    @Test
    public void testCase2() {
        Solution s = new Solution();
        // 4294967293 is too large for int
        // In java, it is -3
        int actual = s.reverseBits(-3 );
        assertEquals(actual, -1073741825);
    }

    @Test
    public void testCase3() {
        Solution s = new Solution();
        int actual = s.reverseBits(-2147483648 );
        assertEquals(actual, 1);
    }

    @Test
    public void testCase4() {
        Solution s = new Solution();
        int actual = s.reverseBits(0 );
        assertEquals(actual, 0);
    }
}