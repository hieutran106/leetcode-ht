package easy._026_remove_duplicates_from_sorted_array;

import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.*;

public class SolutionTest {

    @Test
    public void testCase1() {
        var s = new Solution();
        int[] intput = new int[]{1, 1, 2};
        var actual = s.removeDuplicates(intput);
        Assert.assertEquals(actual, 2);

        int[] newArray = Arrays.copyOfRange(intput, 0, actual);
        Assert.assertArrayEquals(newArray, new int[]{1, 2});

    }

    @Test
    public void testCase2() {
        var s = new Solution();
        int[] intput = new int[]{0,0,1,1,1,2,2,3,3,4};
        var actual = s.removeDuplicates(intput);
        // Assert.assertEquals(actual, 5);
        int[] newArray = Arrays.copyOfRange(intput, 0, 5);
        Assert.assertArrayEquals(newArray, new int[]{0, 1, 2, 3, 4});
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        int[] intput = new int[]{0, 1, 2, 3};
        var actual = s.removeDuplicates(intput);
        // Assert.assertEquals(actual, 4);

        int[] newArray = Arrays.copyOfRange(intput, 0, 4);
        Assert.assertArrayEquals(newArray, new int[]{0, 1, 2, 3});
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        int[] intput = new int[]{};
        var actual = s.removeDuplicates(intput);
        Assert.assertEquals(actual, 0);

    }

    @Test
    public void testCase5() {
        var s = new Solution();
        int[] intput = new int[]{1};
        var actual = s.removeDuplicates(intput);
        Assert.assertEquals(actual, 1);
    }

    @Test
    public void testCase6() {
        var s = new Solution();
        int[] intput = new int[]{1, 2};
        var actual = s.removeDuplicates(intput);
        Assert.assertEquals(actual, 2);
    }
}