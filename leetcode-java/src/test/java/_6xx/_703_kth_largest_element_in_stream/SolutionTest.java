package _6xx._703_kth_largest_element_in_stream;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class SolutionTest {
    @Test
    public void testCase1() {
        int[] arr = {4, 5, 8, 2};
        var solution = new KthLargest(3, arr);
        Assertions.assertEquals(4, solution.add(3));
        Assertions.assertEquals(5, solution.add(5));
        Assertions.assertEquals(5, solution.add(10));
        Assertions.assertEquals(8, solution.add(9));
        Assertions.assertEquals(8, solution.add(4));
    }
}
    