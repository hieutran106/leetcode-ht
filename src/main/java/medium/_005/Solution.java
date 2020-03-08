package medium._005;

public class Solution {

    public String longestPalindrome(String s) {
        if (s.length() ==0) {
            return s;
        }

        int max = 1;
        int[] pos = new int[] {0, 0};

        for (int i=0; i < s.length(); i ++) {
            var check1 = isPalindrome1(i, s, true);
            if (check1[1] - check1[0] +1 > max) {
                System.out.println(String.format("Find palindrome at [%d,%d], palindrome=%s", check1[0], check1[1], s.substring(check1[0], check1[1] + 1)));
                max = check1[1] - check1[0];
                pos[0] = check1[0];
                pos[1] = check1[1];
            }

            check1 = isPalindrome1(i, s, false);
            if (check1[1] - check1[0] +1 > max) {
                System.out.println(String.format("Find palindrome at [%d,%d], palindrome=%s", check1[0], check1[1], s.substring(check1[0], check1[1] + 1)));
                max = check1[1] - check1[0];
                pos[0] = check1[0];
                pos[1] = check1[1];
            }
        }


        return s.substring(pos[0], pos[1] + 1);
    }


    public int[] isPalindrome1(int pos, String s, boolean isOddSubstring) {
        int i = isOddSubstring ? pos - 1 : pos;
        int j = pos + 1;
        int[] result = new int[]{0, -1};
        while (i >= 0 && j <s.length()) {
            if (s.charAt(i) != s.charAt(j)) {
                break;
            }
            result[0] = i--;
            result[1] = j++;
        }
        return  result;
    }

}
