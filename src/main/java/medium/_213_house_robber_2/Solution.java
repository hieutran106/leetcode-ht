package medium._213_house_robber_2;

public class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n ==0) return 0;
        if (n == 1) return nums[0];
        if (n == 2) {
            return Math.max(nums[0], nums[1]);
        }
        // case 1- rob house at 0, not rob at the last
        var case1 = robRange(nums, 0, n - 1);
        // case 2 - not rob at house 1, // might rob at the last
        var case2 = robRange(nums, 1, n);
        return Math.max(case1, case2);
    }

    public int robRange(int nums[], int start, int end) {
        int[] dp = new int[end - start];

        dp[0] = nums[start];
        if (start + 1 >= end) {
            return dp[0];
        } else {
            dp[1] = Math.max(dp[0], nums[start+ 1]);
        }
        // for loop
        for (int i = 2; i < dp.length; i++) {
            dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i + start]);
        }
        return dp[dp.length - 1];
    }
}
