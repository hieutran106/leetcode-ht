package medium._763;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;


// check intersetion of two set (before set and after set) is empty
public class Solution implements ISolution763 {
    public List<Integer> partitionLabels(String s) {
        var result = new ArrayList<Integer>();
        while (s.length() >0) {
            int old = s.length();
            s = helper(s);
            int newString = s.length();
            result.add(old -newString);
        }


        return result;
    }

    private String helper(String s) {

        int lastIndex = s.lastIndexOf(s.charAt(0));
        if (lastIndex <= 1) {
            return s.substring(lastIndex + 1);
        }
        // lastIndex > 1
        int[] mapOne = new int[26];
        int[] mapTwo = new int[26];

        // cal map 1
        for (int i=0; i <= lastIndex; i++) {
            mapOne[s.charAt(i) - 'a']+=1;
        }

        // cal map 2
        for (int i = lastIndex+1; i <s.length();i++) {
            mapTwo[s.charAt(i) - 'a']+=1;
        }

        int step = 1;
        while (!isIntersectionEmpty(mapOne, mapTwo)) {
            int cursor = lastIndex + step;
            mapOne[s.charAt(cursor) - 'a']++;
            mapTwo[s.charAt(cursor) - 'a']--;
            step ++;
        }

        return s.substring(lastIndex + step);
    }

    private boolean isIntersectionEmpty(int[] x, int[] y) {
        int[] z = new int[x.length];
        for (int i =0; i < x.length; i++) {
            z[i] = x[i] * y[i];
            if (z[i] != 0) {
                return false;
            }
        }
        return true;
    }
}
