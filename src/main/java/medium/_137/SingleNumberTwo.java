package medium._137;

import java.util.Arrays;

public class SingleNumberTwo {

    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        for (int i =0; i < nums.length -1; i = i +3) {
            if (nums[i] != nums[i+1])
                return nums[i];
        }
        return nums[nums.length - 1];
    }

    // solution from
    public int singNumberM2(int[] nums) {
        int ones = 0, twos = 0;
        for (int i =0; i < nums.length; i ++) {
            ones = (ones ^ nums[i]) & ~twos;
            twos = (twos ^ nums[i] & ~ones);
        }
        return ones;
    }
}
