package medium._216_combination_sum_3;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        ArrayList result = new ArrayList();
        LinkedList<Integer> path = new LinkedList<>();
        backtrack(path, 1, n, k, result);
        return result;
    }


    private void backtrack(LinkedList<Integer> path, int start, int target, int k, ArrayList result) {
        if (path.size() > k) {
            return;
        }

        if (path.size() ==k && target == 0) {
            // solution found
            var newPath = new ArrayList<>(path);
            result.add(newPath);
            return;
        }

        for (int i= start; i <= 9 ; i++) {
            if (i > target) break;
            path.add(i);
            backtrack(path, i + 1, target - i, k, result);
            path.removeLast();
        }

    }
}
