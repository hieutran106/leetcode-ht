package medium._994_rotting_oranges;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

// Using either ArrayList or LinkedList is fine

public class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int freshCount = 0;
        // Java LinkedList is a double-end queue
        // ArrayList<int[]> queue = new ArrayList<>();
        var queue = new LinkedList<int[]>();
        for (int i = 0; i < rows; i++)
            for (int j =0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    freshCount++;
                } else if (grid[i][j] ==2) {
                    queue.add(new int[]{i, j});
                }
            }

        int times = 0;
        int[][] directions = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while (!queue.isEmpty() && freshCount > 0) {
            times ++;
            //ArrayList<int[]> newQueue = new ArrayList<>();
            int size = queue.size();
            for (int i =0; i < size; i++) {
                //int[] rottenPos = queue.get(i);
                int[] rottenPos = queue.poll();
                grid[rottenPos[0]][rottenPos[1]] = 2;
                // check 4 side, if is fresh --> add to newQeueu, and minus fresh
                for (int[] direction: directions) {
                    int[] position = new int[] {rottenPos[0] + direction[0], rottenPos[1] + direction[1]};
                    int x = position[0];
                    int y = position[1];
                    if (insideBoard(x, y, rows, cols) && grid[x][y] == 1) {
                        // make orange at the position rotten
                        grid[x][y] = 2;
                        //newQueue.add(position);
                        queue.offer(position);
                        freshCount--;
                    }
                }
            }
            // update
            // queue = newQueue;
        }

        if (freshCount > 0) {
            return -1;
        } else {
            return times;
        }
    }

    private boolean insideBoard(int x, int y, int rows, int cols) {
        return x >=0 && x < rows && y >= 0 && y < cols;
    }
}
