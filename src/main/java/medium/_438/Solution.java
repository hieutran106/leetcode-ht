package medium._438;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        var result = new ArrayList<Integer>();
        int m = s.length();
        int n = p.length();
        if (m < n || n ==0) {
            return result;
        }

        for (int i =0; i <= m - n; i ++) {
            var substring = s.substring(i, i + n);
            // check substring is anagram to p
            if (isAnagram(substring, p)) {
                result.add(i);
            }
        }
        return result;
    }

    private boolean isAnagram(String x, String y) {
        var str1= x.toCharArray();
        var str2 = y.toCharArray();
        int[] count = new int[26];
        for (int i =0; i < x.length(); i++) {
            count[str1[i] - 97]++;
            count[str2[i] - 97]--;
        }
        for (int i=0; i < 26;i ++) {
            if (count[i] != 0){
                return false;
            }
        }
        return true;
    }

}
