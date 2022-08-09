package medium._046_permutations;

import java.util.*;

public class Solution {
    public List<List<Integer>> permute(int[] nums) {

        ArrayList result = new ArrayList();
        backtrack2(nums, new LinkedList<>(), result);
        return result;
    }

    // path - recorded in track
    // selection list -> those elements in nums that do no exist in track
    // end condition: all elements in nums appear in track
    private void backtrack2(int[] nums, LinkedList<Integer> path, ArrayList res) {
        if (path.size() == nums.length) {
            res.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (path.contains(num)) {
                continue;
            }
            // select
            path.add(num);
            // backtrack
            backtrack2(nums, path, res);
            // deselect
            path.removeLast();
            // add the selection to the selection list
        }
    }


}
