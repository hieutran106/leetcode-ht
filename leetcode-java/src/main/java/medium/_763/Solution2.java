package medium._763;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution2 implements ISolution763 {

    @Override
    public List<Integer> partitionLabels(String s) {
        List<Integer> list = new ArrayList<>();
        if (s ==null || s.length() ==0) {
            return list;
        }
        int[] map = new int[26];  // record the last index of the each char

        for(int i = 0; i < s.length(); i++){
            map[s.charAt(i)-'a'] = i;
        }

        int last = 0;
        int start = 0;
        for (int  i=0; i < s.length(); i++) {
            last = Math.max(last, map[s.charAt(i) - 'a']);
            if (last ==i) {
                list.add(last - start + 1);
                start = last + 1;
            }
        }
        return list;

    }
}
