package easy._268_missing_number;

public class Solution {
    public int missingNumber(int[] nums) {
        var len = nums.length;
        // sum from 0 to n
        var sum = len * (len +1) /2 ;
        var total = 0;
        for (int i =0; i < nums.length; i++) {
            total += nums[i];
        }
        return sum - total;
    }
}
