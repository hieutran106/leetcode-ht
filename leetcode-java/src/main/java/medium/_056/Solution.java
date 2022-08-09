package medium._056;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Solution {
    public int[][] merge(int[][] intervals) {
        // sort intervals
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] t1, int[] t2) {
                return t1[0] - t2[0];
            }
        });


        int i = 0;
        List result = new ArrayList();
        while (i < intervals.length) {
            int[] currInterval = intervals[i];
            int j = 1;
            while(true) {
                int nextIndex = i + j;
                if (nextIndex == intervals.length) {
                    break;
                }

                int[] next = intervals[i + j];
                if (!isOverlap(currInterval, next)) {
                    break;
                }

                int[] mergeable = intervals[i + j];
                currInterval = merge(currInterval, mergeable);
                j++;
            }

            i = i + j  ;
            result.add(currInterval);
        }

        int[][] arrays = new int[result.size()][2];
        for (int k =0; k < result.size(); k++) {
            int[] cast = (int[])result.get(k);
            arrays[k][0] = cast[0];
            arrays[k][1] = cast[1];
        }
        return arrays;
    }

    private boolean isOverlap(int[] interval1, int[] interval2) {
        return interval1[1] >= interval2[0];
    }

    private int[] merge(int[] interval1, int[] interval2) {
        int[] result = new int[2];
        result[0] = interval1[0];
        result[1] = Math.max(interval1[1], interval2[1]);
        return result;
    }
}
