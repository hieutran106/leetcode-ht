package medium._064;

import java.util.*;



class Point {
    int x;
    int y;

    int distance;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

}

public class MinimumPathSum {

    public int minPathSum(int[][] grid) {
        var n = grid[0].length;
        var m = grid.length;

        PriorityQueue<Point> queue = new PriorityQueue<>((a,b) -> a.distance - b.distance);

        var start = new Point(0, 0);
        start.distance = grid[0][0];

        queue.add(start);

        while (!queue.isEmpty()) {
            var point = queue.poll();

            if (point.x == m -1 && point.y == n - 1) {
                // goal
                return point.distance;
            }

            var adjs = getAdjacien(point, m ,n);

            for (var p : adjs) {
                // check if p is in queue and update
                boolean meet = false;
                for (var qp: queue) {
                    if (p.x == qp.x && p.y == qp.y) {
                        meet = true;
                        if (point.distance + grid[p.x][p.y] < qp.distance) {
                            qp.distance = point.distance + grid[p.x][p.y];
                        }
                    }
                }
                // if not in
                if (meet == false) {
                    p.distance = point.distance + grid[p.x][p.y];
                    queue.add(p);
                }
            }
        }

        return 0;
    }

    private List<Point> getAdjacien(Point p, int m, int n) {
        var result = new ArrayList<Point>();
        var p1 = new Point(p.x +1, p.y);
        var p2 = new Point(p.x, p.y + 1);

        if (isInBoard(p1,m,n))
            result.add(p1);
        if (isInBoard(p2, m,n))
            result.add(p2);
        return result;
    }

    private boolean isInBoard(Point p, int m, int n) {
        var x = p.x;
        var y = p.y;
        var xValid = 0 <= x && x <= m -1;
        var yValid = 0 <= y && y <= n -1;
        return xValid && yValid;
    }

}
