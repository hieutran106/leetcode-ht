package medium._647;

public class Solution {
    public int countSubstrings(String s) {
        if (s.length() ==0) {
            return 0;
        }
        int sum = 0;
        for (int i=0; i < s.length(); i ++) {
            var oddPalin = countPalinSubString(i, s, true);
            var evenPalin = countPalinSubString(i, s, false);
            sum = sum + oddPalin + evenPalin - 1;
        }
        return sum;
    }


    private int countPalinSubString(int pos, String s, boolean isOddSubstring) {
        int i = isOddSubstring ? pos - 1 : pos;
        int j = pos + 1;

        int result = 1;
        while (i >= 0 && j <s.length()) {
            if (s.charAt(i) != s.charAt(j)) {
                break;
            }
            result++;
            i--;
            j++;
        }
        return result;
    }
}
