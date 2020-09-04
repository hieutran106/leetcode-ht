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
            boolean isExist = false;
            for (var result: results) {
                if (isIdentical(path, result)) {
                    isExist = true;
                    break;
                }
            }
            if (!isExist) {
                var solution = new ArrayList<>(path);
                results.add(solution);
            }
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            int candidate = candidates[i];
            if (candidate > target) continue;

            // skip next candidate
            path.add(candidates[i]);
            backtrack(path, i + 1, candidates, target - candidates[i], results);
            path.removeLast();
        }
    }

    private boolean isIdentical(List<Integer> l1, List<Integer> l2) {
        if (l1.size() != l2.size()) {
            return false;
        }
        int size = l1.size();
        for (int i =0; i < size; i++) {
            if (l1.get(i) != l2.get(i))
                return false;
        }
        return true;
    }
}
