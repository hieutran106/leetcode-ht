package medium._078_subsets;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/*
*  Backtracking
* */
public class Solution {
    public List<List<Integer>> subsets2(int[] nums) {
        ArrayList result = new ArrayList();
        LinkedList<Integer> path = new LinkedList<>();
        backtrack(path, 0, nums, result);
        return result;
    }

    private void backtrack(LinkedList<Integer> path, int start, int[] nums, ArrayList result) {
        // no need to check end condition in this case
        var newPath = new LinkedList<>(path);
        result.add(newPath);

        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            backtrack(path, i + 1, nums, result);
            path.removeLast();
        }
    }

    // dynamic programming
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList();
        List<Integer> baseCase = new ArrayList<>();
        result.add(baseCase);

        for (int i =0; i < nums.length; i++) {
            int size = result.size();
            for (int j = 0; j <size;j++) {
                var newList = new ArrayList<>(result.get(j));
                newList.add(nums[i]);

                result.add(newList);
            }
        }
        return result;
    }

}
