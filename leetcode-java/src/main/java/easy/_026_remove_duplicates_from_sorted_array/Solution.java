package easy._026_remove_duplicates_from_sorted_array;

public class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length <= 1) {
            return nums.length;
        }
        int duplication = 0;
        // Marking duplication
        for (int i = nums.length -1; i > 0; i--) {
            if (nums[i] == nums[i-1]) {
                nums[i] = Integer.MAX_VALUE;
                duplication ++;
            }
        }
        // bubble sort
        for (int i=0; i < nums.length -1; i++) {
            boolean swap = false;

            for (int j = 0; j < nums.length - i - 1;j ++) {
                if (nums[j] > nums[j+1]) {
                    int temp = nums[j+1];
                    nums[j+1] = nums[j];
                    nums[j] = temp;
                    swap = true;
                }
            }
            // Early return
            if (!swap) {
                break;
            }
        }
        return nums.length - duplication;
    }
}
