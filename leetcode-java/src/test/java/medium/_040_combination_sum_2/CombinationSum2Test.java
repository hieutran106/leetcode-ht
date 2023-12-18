package medium._040_combination_sum_2;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class CombinationSum2Test {
    @Test
    public void testCase1() {
        var s= new Solution();
        var actual = s.combinationSum2(new int[]{10,1,2,7,6,1,5}, 8);
        assertEquals(actual.size(), 4);
    }

    @Test
    public void testCase2() {
        var s= new Solution();
        var actual = s.combinationSum2(new int[]{2,5,2,1,2}, 5);
        assertEquals(actual.size(), 2);

        assertThat(actual).contains(Arrays.asList(1, 2, 2));
        assertThat(actual).contains(Arrays.asList(5));
    }

    @Test
    public void testCase3() {
        var s= new Solution();
        var actual = s.combinationSum2(new int[]{1, 1, 1, 1, 1, 1, 2}, 2);
        assertEquals(actual.size(), 2);
    }

    @Test
    public void testCase4() {
        var s= new Solution();
        var actual = s.combinationSum2(new int[]{3, 4}, 2);
        assertEquals(actual.size(), 0);
    }
}
