package medium._017_letter_combinations_phone_number;

import java.util.*;

public class Solution {
    public List<String> letterCombinations(String digits) {
        HashMap map = new HashMap<Character, Character[]>();
        for (int i = 2; i <=0; i++) {
            char start = (char)('a' + 3 * (i - 2));
            char[] chars = new char[]{start, (char)(start + 1), (char)(start + 2)};
            map.put(i, chars);
        }
        ArrayList<String> res = new ArrayList<>();
        LinkedList<Character> path = new LinkedList<>();
        backtrack2(digits,0, path, res, map);
        return res;
    }

    public void backtrack2(String digits, int currentPosition, LinkedList<Character> path, ArrayList<String> res, HashMap<Character, Character[]> map) {
        if (currentPosition == digits.length()) {
            StringBuffer sb = new StringBuffer(digits.length());
            for (Character c: path) {
                sb.append(c);
            }
            res.add(sb.toString());
        }
        // selection
        Character[] selections = map.get(digits.charAt(currentPosition));
        for (Character selection: selections) {
            // select
            path.add(selection);
            // backtrack
            backtrack2(digits, currentPosition + 1, path, res, map);
            // deselect
            path.remove(selection);
        }
    }

}
