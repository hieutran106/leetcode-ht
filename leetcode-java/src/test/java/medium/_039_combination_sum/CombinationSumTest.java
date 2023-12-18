package medium._039_combination_sum;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class CombinationSumTest {
    @Test
    public void testCase1() {
        var s = new Solution();
        var actual = s.combinationSum(new int[]{2, 3, 6, 7}, 7);

        assertThat(actual).hasSize(2);
        assertThat(actual).contains(Arrays.asList(3, 2, 2));
        assertThat(actual).contains(Arrays.asList(7));

    }

    @Test
    public void testCase2() {
        var s = new Solution();
        var actual = s.combinationSum(new int[]{2, 3, 5}, 8);
        assertEquals(actual.size(), 3);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.combinationSum(new int[]{8}, 6);
        assertEquals(actual.size(), 0);
    }
}
