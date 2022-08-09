package medium._784_letter_case_permutation;

import java.util.ArrayList;
import java.util.List;

/*
* Backtracking
* */
public class Solution {
    public List<String> letterCasePermutation(String S) {
        ArrayList<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder(S.length());
        backtrack(sb, 0, S, result);
        return result;
    }

    private void backtrack(StringBuilder sb, int start, String s, ArrayList<String> result) {
        if (sb.length() == s.length()) {
            result.add(sb.toString());
            return;
        }
        for (int i = start; i < s.length(); i++) {
            char current = s.charAt(i);
            if ('0' <= current && current <= '9') {
                // current is a digit
                sb.append(current);
                backtrack(sb, i +1, s, result);
                sb.deleteCharAt(sb.length() - 1);
            } else {
                // current is a letter, get lower case and upper case
                // do lower case
                char lowerCase = Character.toLowerCase(current);
                sb.append(lowerCase);
                backtrack(sb, i + 1, s, result);
                sb.deleteCharAt(sb.length() - 1);
                // do upper case
                char upperCase = Character.toUpperCase(current);
                sb.append(upperCase);
                backtrack(sb, i + 1, s, result);
                sb.deleteCharAt(sb.length() - 1);
            }
        }
    }
}
