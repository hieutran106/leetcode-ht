package medium._064;

import javax.swing.plaf.synth.ColorType;
import java.util.*;



class Point {
    int x;
    int y;

    int distance;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object o) {
        Point p = (Point)o;
        return (this.x == p.x && this.y == p.y);
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }
}




class MinimumPathSum {

    private Point getShortest(HashSet<Point> set) {
        Point result = null;
        int min = Integer.MAX_VALUE;
        for (Point p: set) {
            if (p.distance < min) {
                result = p;
                min = p.distance;
            }
        }

        return result;
    }
    public int minPathSum(int[][] grid) {
        var n = grid[0].length;
        var m = grid.length;
        int[][] checked = new int[m][n];
        //PriorityQueue<Point> queue = new PriorityQueue<>((a,b) -> (a.distance - b.distance));
        HashSet<Point> queue = new HashSet<>();

        var start = new Point(0, 0);
        start.distance = grid[0][0];

        queue.add(start);
        while (!queue.isEmpty()) {
            var point = getShortest(queue);

            System.out.println(String.format("Select point [x=%d, y= %d, distance=%d], queue size = %d", point.x, point.y, point.distance, queue.size()));
            if (point.x == m -1 && point.y == n - 1) {
                // goal
                return point.distance;
            }

            var adjs = getAdjacent(point, m ,n);

            for (var p : adjs) {
                if (p == null) {
                    continue;
                }
                var distanceToAdjacent = point.distance + grid[p.x][p.y];

                if (checked[p.x][p.y] == 1) {
                    continue;
                }

                p.distance = distanceToAdjacent;
                queue.add(p);
                checked[p.x][p.y] = 1;
            }
        }
        return 0;
    }

    public int minPathSum1(int[][] grid) {
        var n = grid[0].length;
        var m = grid.length;

        PriorityQueue<Point> queue = new PriorityQueue<>((a,b) -> (a.distance - b.distance));

        var start = new Point(0, 0);
        start.distance = grid[0][0];

        queue.add(start);

        HashSet<Point> set = new HashSet<Point>();


        while (!queue.isEmpty()) {
            var point = queue.poll();
            System.out.println(String.format("Select point [x=%d, y= %d, distance=%d], queue size = %d", point.x, point.y, point.distance, queue.size()));
            if (point.x == m -1 && point.y == n - 1) {
                // goal
                return point.distance;
            }

            var adjs = getAdjacent(point, m ,n);


            for (var p : adjs) {
                if (p == null) {
                    continue;
                }
                // check if p is in queue and update
                boolean meet = false;
                var distanceToAdjacent = point.distance + grid[p.x][p.y];
                for (var qp: queue) {
                    if (p.x == qp.x && p.y == qp.y) {
                        // p is already in queue
                        meet = true;

                        if (distanceToAdjacent < qp.distance) {
                            // wrong
                            //qp.distance = point.distance + grid[p.x][p.y];

                            queue.remove(qp);
                            p.distance = distanceToAdjacent;
                            queue.add(p);
                        }
                        break;
                    }
                }
                // if not in
                if (meet == false) {
                    p.distance = distanceToAdjacent;
                    queue.add(p);
                }
            }



        }

        return 0;
    }



    private List<Point> getAdjacent1(Point p, int m, int n) {
        var result = new ArrayList<Point>();
        var p1 = new Point(p.x +1, p.y);
        var p2 = new Point(p.x, p.y + 1);

        if (isInBoard(p1,m,n))
            result.add(p1);
        if (isInBoard(p2, m,n))
            result.add(p2);
        return result;
    }
    private Point[] getAdjacent(Point p, int m, int n) {

        var result = new Point[2];
        var p1 = new Point(p.x +1, p.y);
        var p2 = new Point(p.x, p.y + 1);

        if (isInBoard(p1,m,n))
            result[0] = p1;
        if (isInBoard(p2, m,n))
            result[1] = p2;
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
