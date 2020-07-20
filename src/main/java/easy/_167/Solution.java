package easy._167;


import java.util.HashMap;

// Dictionary solution
public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

         for (int i =0; i < numbers.length; i ++) {
             int value = numbers[i];
             if (map.containsKey(numbers[i])) {
                 return new int[]{map.get(numbers[i]) + 1, i + 1};
             }
             map.put(target - value,i);
         }
         return new int[]{0, 0};
    }
}

