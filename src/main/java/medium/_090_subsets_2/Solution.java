package medium._090_subsets_2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        ArrayList result = new ArrayList();
        Arrays.sort(nums);
        LinkedList<Integer> path = new LinkedList<>();
        backtrack(path, 0, nums, result);
        return result;
    }

    private void backtrack(LinkedList<Integer> path, int start, int[] nums, ArrayList result) {
        var newPath = new LinkedList<>(path);
        result.add(newPath);

        for (int i = start; i < nums.length; i++) {
            if (i > start && nums[i] == nums[i-1]) continue;
            path.add(nums[i]);
            backtrack(path, i + 1, nums, result);
            path.removeLast();
        }
    }

}
