package medium._022_generate_parentheses;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Solution {
    public List<String> generateParenthesis(int n) {
        if (n ==0) {
            return new ArrayList<>();
        }
        ArrayList<String>[] dp = new ArrayList[n+1];
        // base case
        dp[1] = new ArrayList<String>();
        dp[1].add("()");

        for (int i =2 ; i <=n; i++) {
            dp[i] = new ArrayList<String>();
            ArrayList<String> last = dp[i - 1];
            for (String x: last) {
                dp[i].add("("+x+")");
                dp[i].add("()" + x);
                dp[i].add(x + "()");
            }
            var index = dp[i].indexOf("()".repeat(i));
            dp[i].remove(index);
        }
        ArrayList<String> result = dp[n];
        return result;

    }

}
