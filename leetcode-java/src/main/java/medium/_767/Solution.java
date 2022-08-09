package medium._767;

import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class Solution {
    public String reorganizeString(String S) {
        Map<Character, Integer> map = new HashMap<>();
        for(char c: S.toCharArray()){
            map.put(c, map.getOrDefault(c,0)+1);
        }

        PriorityQueue<Map.Entry<Character, Integer>> maxHeap = new PriorityQueue<>(new Comparator<Map.Entry<Character, Integer>>() {
            @Override
            public int compare(Map.Entry<Character, Integer> t1, Map.Entry<Character, Integer> t2) {
                return t2.getValue() - t1.getValue();
            }
        });

        maxHeap.addAll(map.entrySet());

        var maxFreq = maxHeap.peek().getValue();
        if (2 * maxFreq -1 > S.length()) {
            return "";
        }

        // construct new string
        char[] result = new char[S.length()];
        // fill in even index, then odd index --> 0,2,4,6... 1,3,5,7
        int index = 0;
        while (!maxHeap.isEmpty()) {
            var entry = maxHeap.poll();
            char currChar = entry.getKey();
            int freq = entry.getValue();
            for (int j=0; j < freq; j++) {
                result[index] = currChar;
                index += 2;
                if (index >= result.length) {
                    // switch to odd index
                    index = 1;
                }
            }
        }

        return new String(result);
    }
}
