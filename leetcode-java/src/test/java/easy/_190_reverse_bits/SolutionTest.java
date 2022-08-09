package easy._190_reverse_bits;

import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.*;

public class SolutionTest {

    @Test
    public void testCase1() {
        Solution s = new Solution();
        int actual = s.reverseBits(43261596 );
        Assert.assertEquals(actual, 964176192);
    }

    @Test
    public void testCase2() {
        Solution s = new Solution();
        // 4294967293 is too large for int
        // In java, it is -3
        int actual = s.reverseBits(-3 );
        Assert.assertEquals(actual, -1073741825);
    }

    @Test
    public void testCase3() {
        Solution s = new Solution();
        int actual = s.reverseBits(-2147483648 );
        Assert.assertEquals(actual, 1);
    }

    @Test
    public void testCase4() {
        Solution s = new Solution();
        int actual = s.reverseBits(0 );
        Assert.assertEquals(actual, 0);
    }
}