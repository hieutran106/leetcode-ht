package medium._039_combination_sum;

import org.junit.Assert;
import org.junit.Test;

import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;

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
        Assert.assertEquals(actual.size(), 3);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        var actual = s.combinationSum(new int[]{8}, 6);
        Assert.assertEquals(actual.size(), 0);
    }
}
