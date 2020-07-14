package medium._063;

// Dynamic programming
public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        if (m ==0) {
            return 0;
        }
        int[][] matrix = new int[m][n];
        for (int i =0; i < m; i++)
            for (int j=0; j < n; j++) {
                if (obstacleGrid[i][j] == 1) {
                    matrix[i][j] = 0;
                } else if (i ==0 && j==0) {
                    matrix[i][j] = 1;
                } else if (i ==0) {
                    matrix[i][j] = matrix[i][j-1];
                } else if (j==0) {
                    matrix[i][j] = matrix[i-1][j];
                } else
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1];
            }
        return matrix[m-1][n-1];
    }
}
