package medium._542;


// Use dynamic programming
public class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        // handle corner case

        int maxDistance = row + col - 2;

        int[][] result = new int[row][col];
        for (int i =0; i < row; i++)
            for (int j =0; j < col; j++) {
                if (matrix[i][j] ==0) {
                    result[i][j] = 0;
                } else {
                    int topValue = i - 1 >= 0 ? result[i-1][j] : maxDistance;
                    int leftValue = j - 1 >= 0 ? result[i][j-1]: maxDistance;
                    result[i][j] = Math.min(topValue, leftValue) + 1;
                }
            }

        for (int i = row - 1; i >=0; i--)
            for (int j = col -1; j >= 0; j--) {
                if (matrix[i][j] == 0) {
                    result[i][j] = 0;
                } else {
                    int bottomValue = i + 1 < row ? result[i+1][j] : maxDistance;
                    int rightValue = j + 1 < col ? result[i][j+1]: maxDistance;
                    result[i][j] = Math.min(Math.min(bottomValue, rightValue), result[i][j] - 1) + 1;
                }
            }

        return result;
    }
}
