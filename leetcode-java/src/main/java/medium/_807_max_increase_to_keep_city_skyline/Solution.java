package medium._807_max_increase_to_keep_city_skyline;

import java.util.Arrays;

public class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int[] maxVertical = maxVertical(grid);
        int[] maxHorizontal = maxHorizontal(grid);

        int n = grid.length;
        int sum = 0;

        for (int i =0; i < n; i++) {
            for (int j =0; j < n; j++) {
                int a = maxVertical[j];
                int b = maxHorizontal[i];
                int min = Math.min(a, b);
                if (min > grid[i][j]) {
                    sum += min - grid[i][j];
                }
            }
        }

        return sum;
    }

    public int[] maxVertical(int[][] grid) {
        int n = grid.length;
        int[] result = new int[n];
        for (int i =0; i < n;i++) {
            int max = grid[0][i];
            for (int j =0; j < n; j++) {
                if (grid[j][i] > max) {
                    max = grid[j][i];
                }
            }
            result[i] = max;
        }
        return result;
    }

    public int[] maxHorizontal(int[][] grid) {
        int n = grid.length;
        int[] result = new int[n];
        for (int i =0; i < n;i++) {
            int max = grid[i][0];
            for (int j =0; j < n; j++) {
                if (grid[i][j] > max) {
                    max = grid[i][j];
                }
            }
            result[i] = max;
        }
        return result;
    }
}
