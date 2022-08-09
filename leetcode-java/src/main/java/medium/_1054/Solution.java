package medium._1054;

import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class Solution {
    public int[] rearrangeBarcodes(int[] barcodes) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int c: barcodes){
            map.put(c, map.getOrDefault(c,0)+1);
        }

        PriorityQueue<Map.Entry<Integer, Integer>> maxHeap = new PriorityQueue<>(new Comparator<Map.Entry<Integer, Integer>>() {
            @Override
            public int compare(Map.Entry<Integer, Integer> t1, Map.Entry<Integer, Integer> t2) {
                return t2.getValue() - t1.getValue();
            }
        });

        maxHeap.addAll(map.entrySet());

        // construct new string
        int[] result = new int[barcodes.length];
        // fill in even index, then odd index --> 0,2,4,6... 1,3,5,7
        int index = 0;
        while (!maxHeap.isEmpty()) {
            var entry = maxHeap.poll();
            int currChar = entry.getKey();
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

        return result;
    }
}
