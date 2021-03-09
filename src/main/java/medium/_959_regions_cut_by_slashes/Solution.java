package medium._959_regions_cut_by_slashes;

public class Solution {
    public int regionsBySlashes(String[] grid) {
        int[][] upscale = this.upscale(grid);
        return this.countRegions(upscale);
    }

    private int countRegions(int[][] grid) {
        int numRegions = 0;
        int n = grid.length;
        for (int r =0; r <n;r ++){
            for (int c =0; c<n; c++) {
                int curr = grid[r][c];
                if (curr == 0) {
                    numRegions++;
                    this.dfs(r, c, grid, n);
                }
            }
        }
        return numRegions;
    }

    private void dfs(int r, int c, int[][] grid, int n) {
        if (r<0 || r>=n || c<0 || c >=n) {
            return;
        }
        if (grid[r][c] !=0) {
            return;
        }
        grid[r][c] = -1;
        this.dfs(r+1, c, grid, n);
        this.dfs(r-1, c, grid, n);
        this.dfs(r, c+1, grid, n);
        this.dfs(r, c-1, grid, n);
    }

    private int[][] upscale(String[] grid) {
        int n = grid.length;
        int[][] upscale = new int[3 * n][3 * n];
        for (int i =0; i < n; i++) {
            for (int j=0; j < n;j++) {
                char currChar = grid[i].charAt(j);
                if (currChar == ' ') {
                    continue;
                }
                this.fillSlash(upscale, i, j, currChar == '/');
            }
        }
        return upscale;
    }

    private void fillSlash(int[][] upscale, int row, int col, boolean isForwardSlash) {
        int startRow = row * 3;
        int startCol = col * 3;

        upscale[startRow+1][startCol+1] = 1;

        if (isForwardSlash) {
            upscale[startRow][startCol+2] = 1;
            upscale[startRow+2][startCol] = 1;
        } else {
            // backward
            upscale[startRow][startCol] = 1;
            upscale[startRow+2][startCol+2] = 1;
        }
    }


}
