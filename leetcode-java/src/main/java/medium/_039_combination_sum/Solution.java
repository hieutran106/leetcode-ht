package medium._039_combination_sum;

import java.util.*;
import java.util.stream.IntStream;

/* Link: https://leetcode.com/problems/combination-sum/
*  tag: Backtracking
* */
public class Solution {

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        // sort candidates in descending order
        var sortedCandidates = IntStream.of(candidates)
                                .boxed()
                                .sorted(Comparator.reverseOrder())
                                .mapToInt(i -> i).toArray();
        ArrayList result = new ArrayList();
        LinkedList<Integer> path = new LinkedList<>();
        backtrack(path, 0, sortedCandidates, target, result);
        return result;
    }

    private void backtrack(LinkedList<Integer> path, int start, int[] sortedCandidates, int target, ArrayList result) {

        if (target == 0) {
            // solution found
            var newPath = new ArrayList<>(path);
            result.add(newPath);
            return;
        }

        for (int i= start; i < sortedCandidates.length; i++) {
            var candidate = sortedCandidates[i];
            if (candidate > target) continue;
            path.add(candidate);
            backtrack(path, i, sortedCandidates, target - candidate, result);
            path.removeLast();
        }

    }

}
