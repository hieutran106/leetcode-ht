package medium._1054;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

public class DistantBarcodesTest {
    @Test
    public void testCase1() {
        var input = new int[]{1,1,1,2,2,2};
        var s = new Solution();
        var actuals = s.rearrangeBarcodes(input);
        assertArrayEquals(actuals, new int[]{1,2,1,2,1,2});
    }

    @Test
    public void testCase2() {
        var input = new int[]{1,1,1,1,2,2,3,3};
        var s = new Solution();
        var actuals = s.rearrangeBarcodes(input);
        System.out.println(Arrays.toString(actuals));
        assertArrayEquals(actuals, new int[]{1, 3, 1, 3, 1, 2, 1, 2});
    }
}
