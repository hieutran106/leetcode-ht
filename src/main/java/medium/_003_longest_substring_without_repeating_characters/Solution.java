package medium._003_longest_substring_without_repeating_characters;

import java.util.HashMap;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int right = 0;
        int maxLen = 0;
        HashMap<Character, Integer> window = new HashMap<>();

        while (right < s.length()) {
            char c = s.charAt(right);
            // update window
            var count = window.getOrDefault(c, 0);
            if (count == 0) {
                window.put(c, 1);
                // udpate maxLen
                if (window.size() > maxLen) {
                    maxLen = window.size();
                }
            } else if (count == 1) {
                // If the character is already in window, move the left pointer to
                // the right of the same character last found
                while (left < s.length()) {
                    char c2 = s.charAt(left);
                    if (c2 != c) {
                        // remove c2 from window
                        window.remove(c2);
                    } else {
                        // move left to the right of the same char
                        left = left + 1;
                        break;
                    }
                    left ++;
                }

            }

            right++;

        }

        return maxLen;
    }
}
