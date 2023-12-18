package medium._215;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class KthLargestElementTest {
    @Test
    public void testCase1() {
        var solution = new KthLargestElement();
        var input = new int[]{3,2,1,5,6,4};
        var result = solution.findKthLargest(input, 2);
        assertEquals(result, 5);

    }

    @Test
    public void testCase2() {
        var solution = new KthLargestElement();
        var input = new int[]{3,2,3,1,2,4,5,5,6};
        var result = solution.findKthLargest(input, 4);
        assertEquals(4, result);
    }

}
