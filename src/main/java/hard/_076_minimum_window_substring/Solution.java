package hard._076_minimum_window_substring;

import java.util.HashMap;

public class Solution {
    public String minWindow(String s, String t) {

        String res = s;
        int start = 0;
        int left = 0;
        int right = 0;
        int minLen = Integer.MAX_VALUE;

        // needs records the number of occurrences of characters in T
        HashMap<Character, Integer> needs = new HashMap<>();
        // window record the number of corresponding character
        HashMap<Character, Integer> window = new HashMap<>();

        // init needs dictionary
        for (int i =0; i < t.length(); i++) {
            char c = t.charAt(i);
            int count = needs.getOrDefault(c, 0);
            needs.put(c, count + 1);
        }

        // number of characters that match requirement
        int match = 0;

        while (right < s.length()) {
            char c1 = s.charAt(right);
            if (needs.containsKey(c1)) {
                // add char to windows
                int count = window.getOrDefault(c1, 0);
                window.put(c1, count + 1);

                int windowValue = (int)window.get(c1);
                int needsValue = (int)needs.get(c1);

                if (windowValue == needsValue) {
                    // the number of occurences of character c1 meets the require ment
                    match++;
                    System.out.println(match);
                }
            }

            right ++;

            // when we found a valid window, move left to find smaller window
            while (match == needs.size()) {
                // If the window's substring is shorter, update the res
                if (right - left < minLen) {
                    start = left;
                    minLen = right - left;
                }
                // increase the left pointer to make it invalid/ valid again
                char c2 = s.charAt(left);
                if (needs.containsKey(c2)) {
                    // remove from window
                    window.put(c2, window.get(c2) - 1);

                    if (window.get(c2) < needs.get(c2)) {
                        match --;
                    }
                }

                left++;
            }

        }

        return minLen == Integer.MAX_VALUE ? "" : s.substring(start, start + minLen);
    }
}
