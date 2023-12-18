package medium._238;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import org.junit.jupiter.api.Test;

public class ProductOfArrayTests {
    @Test
    public void testCase1() {
        int[] input = new int[] {1, 2, 3, 4};
        var solution = new ProductOfArray();
        var result = solution.productExceptSelf(input);
        assertArrayEquals(new int[]{24, 12, 8,6}, result);
    }

    @Test
    public void testCase2() {
        int[] input = new int[] {5, 1, 1, 1};
        var solution = new ProductOfArray();
        var result = solution.productExceptSelf(input);
        assertArrayEquals(new int[]{1, 5, 5, 5}, result);
    }

    @Test
    public void testCase3() {
        int[] input = new int[] {2, 3, 1};
        var solution = new ProductOfArray();
        var result = solution.productExceptSelf(input);
        assertArrayEquals(new int[]{3, 2, 6}, result);
    }

}
