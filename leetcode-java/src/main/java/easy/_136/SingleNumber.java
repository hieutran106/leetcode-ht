package easy._136;

import java.util.Arrays;

public class SingleNumber {

    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        for (int i =0; i < nums.length; i = i +2) {
            if (nums[i] != nums[i+1])
                return nums[i];
        }
        return -1;

    }

}
