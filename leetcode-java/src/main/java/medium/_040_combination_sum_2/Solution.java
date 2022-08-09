package medium._040_combination_sum_2;

import java.util.*;

public class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);

        ArrayList result = new ArrayList();
        LinkedList<Integer> path = new LinkedList<>();

        backtrack(path, 0, candidates, target, result);
        return result;
    }

    private void backtrack(LinkedList<Integer> path, int start, int[] candidates, int target, List<List<Integer>> results) {
        if (target == 0) {
            var solution = new ArrayList<>(path);
            results.add(solution);
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            int candidate = candidates[i];
            if (candidate > target) continue;
            // avoid duplicate
            // (i > start) means the current number has been added before
            if (i > start && candidates[i] == candidates[i - 1]) continue;
            // skip next candidate
            path.add(candidates[i]);
            backtrack(path, i + 1, candidates, target - candidates[i], results);
            path.removeLast();
        }
    }

}
