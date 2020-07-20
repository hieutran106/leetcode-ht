package medium._347;

import java.util.*;

public class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int n: nums){
            map.put(n, map.getOrDefault(n,0)+1);
        }

        // corner case
        List<Integer>[] buckets = new List[nums.length + 1];
        for (int n: map.keySet()) {
            int fre = map.get(n);
            if (buckets[fre] == null) {
                buckets[fre] =new ArrayList<>();
            }
            buckets[fre].add(n);
        }

        ArrayList<Integer> result = new ArrayList<>();
        // get top K element
        for (int i = buckets.length -1; i>=0 && k > 0; i--) {
            if (buckets[i] !=null) {
                result.addAll(buckets[i]);
                k = k - buckets[i].size();
            }
        }


        return result.stream().mapToInt(i -> i).toArray();
    }
}
