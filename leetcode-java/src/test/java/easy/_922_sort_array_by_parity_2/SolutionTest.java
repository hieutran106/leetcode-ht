package easy._922_sort_array_by_parity_2;

import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.*;

public class SolutionTest {

    @Test
    public void testCase1() {
        Solution s = new Solution();
        int[] input = new int[]{2, 3};
        int[] output = s.sortArrayByParityII(input);
        boolean pass = satisfy(output);
        Assert.assertTrue(pass);
    }

    @Test
    public void testCase2() {
        Solution s = new Solution();
        int[] input = new int[]{4, 2, 5, 7};
        int[] output = s.sortArrayByParityII(input);
        boolean pass = satisfy(output);
        Assert.assertTrue( pass );
    }

    @Test
    public void testCase3() {
        Solution s = new Solution();
        int[] input = new int[]{3, 4};
        int[] output = s.sortArrayByParityII(input);
        boolean pass = satisfy(output);
        Assert.assertTrue(pass);
    }

    @Test
    public void testCase4() {
        Solution s = new Solution();
        int[] input = new int[]{3, 3, 4, 4, 4, 3};
        int[] output = s.sortArrayByParityII(input);
        boolean pass = satisfy(output);
        Assert.assertTrue(pass);
    }

    @Test
    public void testCase5() {
        Solution s = new Solution();
        int[] input = new int[]{2,3,1,1,4,0,0,4,3,3};
        int[] output = s.sortArrayByParityII(input);
        boolean pass = satisfy(output);
        Assert.assertTrue(pass);
    }

    public boolean satisfy(int[] nums) {
        boolean result = true;
        for (int i=0; i < nums.length; i++) {
            boolean index = i %2 ==0;
            boolean value = nums[i] %2 ==0;
            if (index != value) {
                result = false;
                break;
            }
        }
        return result;
    }
}