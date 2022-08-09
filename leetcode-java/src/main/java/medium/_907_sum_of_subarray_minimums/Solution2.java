package medium._907_sum_of_subarray_minimums;

import java.util.Stack;

public class Solution2 implements ISolution {
    public int sumSubarrayMins(int[] arr) {
        long sum = 0;
        long mod = (long)1e9 + 7;
        int[] left = previousSmallerRange(arr);
        int[] right = nextSmallerElementRange(arr);

        for (int i =0; i < arr.length; i++) {
            sum = (sum + (long)arr[i] * left[i] * right[i]) % mod;
        }
        return (int)sum;
    }

    public int[] previousSmallerRange(int[] arr) {
        var len = arr.length;

        int[] result = new int[len];
        var s = new Stack<Integer>();
        // because we need to find next smaller
        // then we need increasing stack
        // but we traverse the input array in reverse order
        for (int i = len - 1; i >=0; i--) {
            result[i] = i + 1;
            while (s.size() > 0 && arr[i] <= arr[s.peek()]) {
                var top = s.pop();
                result[top] = top - i ;
            }
            s.push(i);
        }
        return result;
    }

    public int[] nextSmallerElementRange(int[] arr) {
        int[] result = new int[arr.length];
        var s = new Stack<Integer>();
        // because we need to find next smaller
        // then we need increasing stack
        for (int i =0; i < arr.length; i++) {
            result[i] = arr.length - i;
            while (s.size() > 0 && arr[i] < arr[s.peek()]) {
                var top = s.pop();
                result[top] = i - top;
            }
            s.push(i);
        }
        return result;
    }


}
