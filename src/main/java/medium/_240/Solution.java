package medium._240;

public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length;
        if (row == 0) {
            return false;
        }
        int col = matrix[0].length;
        // start search from top, right corner
        int i = 0;
        int j = matrix[0].length - 1;
        while (i < row && j >=0) {
            if (matrix[i][j] > target) {
                j--;
            } else if (matrix[i][j] < target) {
                i++;
            } else if (matrix[i][j] == target) {
                return true;
            }
        }


        // otherwise return value
        return false;

    }



}
