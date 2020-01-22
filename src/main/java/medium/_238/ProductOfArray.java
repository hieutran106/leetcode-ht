package medium._238;

import java.util.Arrays;
import java.util.stream.IntStream;

public class ProductOfArray {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];

        int[] head = new int[nums.length];
        int[] tail = new int[nums.length];

        head[0] = 1;
        tail[0] = 1;

        for (int i =1; i < nums.length; i ++) {
            head[i] = nums[i-1] * head[i -1];
            int j = nums.length - i;
            tail[i] = nums[j] * tail[i-1];
        }

        for (int i =0; i < nums.length; i ++) {
            int j =  (nums.length-1) -i;
            result[i] = head[i] * tail[j];
        }

        return result;
    }

}
