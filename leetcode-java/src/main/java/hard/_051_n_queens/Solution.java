package hard._051_n_queens;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 * Backtracking
 */
public class Solution {
    public List<List<String>> solveNQueens(int n) {
        ArrayList<List<int[]>> result = new ArrayList<>();
        LinkedList<int[]> path = new LinkedList<>();
        backtrack(path, 0, n, result);

        ArrayList<List<String>> formattedResult = new ArrayList<>();
        for (List<int[]> solution: result) {
            List<String> s = new ArrayList<>();
            for (int[] queen: solution) {
                StringBuilder sb = new StringBuilder(n);
                sb.append(".".repeat(n));
                sb.setCharAt(queen[1], 'Q');
                s.add(sb.toString());
            }
            formattedResult.add(s);
        }
        return formattedResult;
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
