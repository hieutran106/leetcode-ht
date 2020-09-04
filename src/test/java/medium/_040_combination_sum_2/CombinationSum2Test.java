package medium._040_combination_sum_2;

import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;

import static org.assertj.core.api.Assertions.assertThat;

public class CombinationSum2Test {
    @Test
    public void testCase1() {
        var s= new Solution();
        var actual = s.combinationSum2(new int[]{10,1,2,7,6,1,5}, 8);
        Assert.assertEquals(actual.size(), 4);
    }

    @Test
    public void testCase2() {
        var s= new Solution();
        var actual = s.combinationSum2(new int[]{2,5,2,1,2}, 5);
        Assert.assertEquals(actual.size(), 2);

        assertThat(actual).contains(Arrays.asList(1, 2, 2));
        assertThat(actual).contains(Arrays.asList(5));
    }

    @Test
    public void testCase3() {
        var s= new Solution();
        var actual = s.combinationSum2(new int[]{1, 1, 1, 1, 1, 1, 2}, 2);
        Assert.assertEquals(actual.size(), 2);
    }

    @Test
    public void testCase4() {
        var s= new Solution();
        var actual = s.combinationSum2(new int[]{3, 4}, 2);
        Assert.assertEquals(actual.size(), 0);
    }
}
