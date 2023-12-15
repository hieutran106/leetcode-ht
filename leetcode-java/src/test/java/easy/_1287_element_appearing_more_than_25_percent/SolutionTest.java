package easy._1287_element_appearing_more_than_25_percent;
import org.junit.Assert;
import org.junit.Test;

public class SolutionTest {
    public static class Solution {
        public int findSpecialInteger(int[] arr) {
            double threshold = Math.ceil(arr.length / 4.0f);
            int res = arr[0];
            int count = 1;
            for (int i = 1; i < arr.length; i++) {
                if (arr[i] == arr[i-1]) {
                    count++;
                } else {
                    count = 1;
                }
                if (count >= threshold) {
                    res = arr[i];
                    break;

                }
            }
            return res;
        }
    }

    @Test
    public void testCase1() {
        var s = new Solution();
        int actual = s.findSpecialInteger(new int[]{1,2,2,6,6,6,6,7,10});
        Assert.assertEquals(actual, 6);
    }

    @Test
    public void testCase2() {
        var s = new Solution();
        int actual = s.findSpecialInteger(new int[]{1,1});
        Assert.assertEquals(actual, 1);
    }

    @Test
    public void testCase3() {
        var s = new Solution();
        int actual = s.findSpecialInteger(new int[]{2});
        Assert.assertEquals(actual, 2);
    }

    @Test
    public void testCase4() {
        var s = new Solution();
        int actual = s.findSpecialInteger(new int[]{0});
        Assert.assertEquals(actual, 0);
    }

}