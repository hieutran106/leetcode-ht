package medium._022_generate_parentheses;


import java.util.*;

/*
*   Backtracking
*
*
*/

public class Solution {
    public List<String> generateParenthesis(int n) {
        ArrayList<String> list = new ArrayList<>();
        backtrack(n, n, "", list);
        return list;
    }

    private void backtrack(int l, int r, String s, List<String> list) {
        System.out.println(s);
        if (l > r) return; // The number of '(' should be always greater or equal the number of ')'
        if (l ==0 && r == 0) {
            list.add(s);
            return;
        }

        if (l > 0) backtrack(l -1, r, s + "(", list);
        if (r > 0) backtrack(l, r -1 , s + ")", list);
    }

}
