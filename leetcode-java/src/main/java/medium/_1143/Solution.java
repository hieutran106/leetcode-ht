package medium._1143;

public class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int n = text1.length();
        int m = text2.length();
        int[][] l = new int[n+1][ m+1];
        for (int j =0; j <n ; j++) {
            for (int k =0; k < m; k++) {
                if (text1.charAt(j) == text2.charAt(k)) {
                    l[j+1][k+1] = l[j][k] +1;
                } else {
                    l[j+1][k+1] = Math.max(l[j][k+1], l[j+1][k]);
                }
            }
        }

        return l[n][m];
    }
    public static int helper(String x, String y) {
        int n = x.length();
        int m = y.length();
        int[][] l = new int[n+1][ m+1];
        for (int j =0; j <n ; j++) {
            for (int k =0; k < m; k++) {
                if (x.charAt(j) == y.charAt(k)) {
                    l[j+1][k+1] = l[j][k] +1;
                } else {
                    l[j+1][k+1] = Math.max(l[j][k+1], l[j+1][k]);
                }
            }
        }

        return l[n][m];
    }
}
