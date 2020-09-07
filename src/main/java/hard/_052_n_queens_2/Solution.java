package hard._052_n_queens_2;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Solution {
    public int totalNQueens(int n) {
        ArrayList<List<int[]>> result = new ArrayList<>();
        LinkedList<int[]> path = new LinkedList<>();
        backtrack(path, 0, n, result);
        return result.size();
    }

    private void backtrack(LinkedList<int[]> path, int start, int n, ArrayList result) {
        if (path.size() == n) {
            result.add(new ArrayList<>(path));
            return;
        }
        // get selection list given path
        ArrayList<int[]> selectionList = new ArrayList<int[]>();
        for (int col =0; col < n; col++) {
            int[] current = new int[]{start, col};
            if (!isCaptured(current, path)) {
                selectionList.add(current);
            }
        }
        for (var selection: selectionList) {
            path.add(selection);
            backtrack(path, start + 1, n, result);
            path.removeLast();
        }

    }

    private boolean isCaptured(int[] current, List<int[]> queens) {
        for (var queen: queens) {
            // capture by col
            if (queen[1] == current[1]) {
                return true;
            }
            // capture by diagonal
            if (Math.abs(queen[0] - current[0]) == Math.abs(queen[1] - current[1])) {
                return true;
            }
        }
        return false;
    }
}
