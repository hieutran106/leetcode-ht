package medium._077_combinations;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/*
* Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
* You may return the answer in any order.
*
*
 */
public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        ArrayList result = new ArrayList();
        LinkedList<Integer> path = new LinkedList<>();
        backtrack(path, 1, n, k, result);
        return result;
    }

    private void backtrack(LinkedList<Integer> path, int start, int n, int k, ArrayList result) {
        if (path.size() == k) {
            result.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i <=n; i++) {
            path.add(i);
            backtrack(path, i + 1, n, k, result);
            path.removeLast();
        }
    }
}
