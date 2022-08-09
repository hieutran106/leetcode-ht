package medium._063;


// back tracking
public class SolutionBacktracking {

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int pathCount = 0;
        int[] start = new int[]{0,0};

        if (obstacleGrid[m -1][n -1] == 1 || obstacleGrid[0][0] == 1) {
            return 0;
        }

        int[][] cache = new int[m][n];
        for (int i=0; i < m; i ++)
            for (int j=0; j < n; j++) {
                cache[i][j] = -1;
            }

        pathCount = countPathUtils(start, pathCount, obstacleGrid, cache);
        return pathCount;
    }

    private int countPathUtils(int[] curr, int pathCount, int[][] obstacleGrid, int[][] cache) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        if (curr[0] == m -1 && curr[1] == n -1) {
            pathCount++;
            return pathCount;
        }


        int[][] deltas = new int[][]{{1,0}, {0, 1}};
        for (int[] delta: deltas) {
            int[] neighbor = new int[]{curr[0] + delta[0], curr[1] + delta[1]};
            if (!isValidPosition(neighbor, obstacleGrid)) {
                continue;
            }
            pathCount = countPathUtils(neighbor, pathCount, obstacleGrid, cache);
        }
        return pathCount;
    }

    private boolean isValidPosition(int[] pos, int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;

        return pos[0] < m && pos[1] < n && obstacleGrid[pos[0]][pos[1]] != 1;
    }
}
