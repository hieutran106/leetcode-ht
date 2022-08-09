package hard._072_edit_distance;

class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        int[][] dp = new int[m + 1][n +1];

        // base case
        for (int i = 1; i <=m; i++) {
            dp[i][0] = i;
        }

        for (int j = 1; j <=n; j++) {
            dp[0][j] = j;
        }

        for (int i=1; i <=m; i++)
            for (int j=1; j<=n; j++) {
                if (word1.charAt(i -1) == word2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1]; // skip
                } else {
                    int insert = dp[i-1][j] + 1;
                    int replace = dp[i-1][j-1] + 1;
                    int delete = dp[i][j -1] + 1;
                    dp[i][j] = min(insert, replace, delete);
                }
            }

        return dp[m][n];
    }

    private int min(int a, int b, int c) {
        return Math.min(a, Math.min(b, c));
    }
}