package easy._922_sort_array_by_parity_2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;

public class Solution {

    public int[] sortArrayByParityII(int[] nums) {
        int len = nums.length;
        Stack<Integer> stack = new Stack<>();
        for (int i =0; i < len; i++) {
            boolean value = nums[i] %2 ==0;
            boolean index = i % 2 ==0;
            if (value == index) {
                continue;
            }

            if (stack.size() ==0) {
                stack.push(i);
                continue;
            }

            Integer top = stack.peek();
            if ((nums[i] + nums[top]) % 2 ==0) {
                stack.push(i);
            } else {
                // swap
                int j = stack.pop();
                int temp = nums[j];
                nums[j] = nums[i];
                nums[i] = temp;
            }
        }

        return nums;
    }

    public int[] sortArrayByParityII4(int[] nums) {
        ArrayList<Integer> list1 = new ArrayList<>();
        ArrayList<Integer> list2 = new ArrayList<>();

        for (int i =0; i < nums.length;i++) {
            boolean value = nums[i] %2 ==0;
            boolean index = i % 2 ==0;
            if (value == index) {
                continue;
            }

            if (value && !index) {
                list1.add(i);
            } else {
                list2.add(i);
            }
        }

        for (int i =0; i < list1.size();i++) {
            int j = list1.get(i);
            int k = list2.get(i);
            // swap
            int temp = nums[j];
            nums[j] = nums[k];
            nums[k] = temp;
        }

        return nums;
    }


    public int[] sortArrayByParityII3(int[] nums) {
        int len = nums.length;
        for (int i =0; i < len -1 ; i++) {
            boolean index = i % 2 ==0;
            boolean value = nums[i] % 2 == 0;
            if (index == value) {
                // match
                continue;
            }
            int swapIndex = -1;
            for (int j = i+1; j < len; j++) {
                boolean nextValue = nums[j] % 2 ==0;
                if (nextValue == index) {
                    swapIndex = j;
                    break;
                }
            }
            if (swapIndex > 0) {
                int temp = nums[i];
                nums[i] = nums[swapIndex];
                nums[swapIndex] = temp;
            }
        }
        return nums;
    }

    public int[] sortArrayByParityII2(int[] nums) {

        int[] evenFirst = Arrays.stream(nums).boxed().sorted((a, b) -> {
            boolean first = (int)a % 2 ==0;
            boolean second = (int)b %2 == 0;
            if (first == second) {
                return 0;
            }

            if (first && !second) {
                return -1;
            } else {
                return 1;
            }

        }).mapToInt(i -> i).toArray();

        int len = evenFirst.length;
        for (int i = 1; i < evenFirst.length / 2; i = i +2) {
            // swap i-th with length - 1 - i
            int temp = evenFirst[i];
            evenFirst[i] = evenFirst[len -1 - i];
            evenFirst[len -1 - i] = temp;
        }
        return evenFirst;
    }
}
