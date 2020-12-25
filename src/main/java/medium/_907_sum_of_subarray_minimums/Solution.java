package medium._907_sum_of_subarray_minimums;

public class Solution implements ISolution {
    public int sumSubarrayMins(int[] arr) {
        var n = arr.length;
        long sum = 0;
        long mod = (long)1e9 + 7;
        for (int i=0; i < n; i++) {
            // Find step to the left
            int left = 1;
            while ((i-left >=0) && (arr[i-left] > arr[i])) {
                left += 1;
            }
            left -= 1;

            int right = 1;
            while ((i + right < n) && (arr[i+right] >= arr[i])) {
                right += 1;
            }
            right -= 1;

            var number = (left + 1) * (right + 1);
            sum = (sum + (long)arr[i] * number) % mod;

        }
        return (int)(sum);

    }
}
