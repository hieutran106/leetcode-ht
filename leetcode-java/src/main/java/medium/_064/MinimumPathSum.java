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

    public Point(int x, int y, int distance) {
        this(x, y);
        this.distance = distance;
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




class MinimumPathSum implements MinimumPathSumSolution {

    private void addPointToQueue(Point p, PriorityQueue<Point> queue, int[][] visited) {
        visited[p.x][p.y] = 1;
        queue.add(p);
    }

    public int minPathSum(int[][] grid) {
        var m = grid.length;
        var n = grid[0].length;

        var visited = new int[m][n];

        PriorityQueue<Point> queue = new PriorityQueue<>((a,b) -> a.distance - b.distance);
        var start = new Point(0,0, grid[0][0]);

        addPointToQueue(start, queue, visited);

        while(!queue.isEmpty()) {
            Point current = queue.poll();
            if (current.x == m-1 && current.y == n-1) {
                // reach destination
                return current.distance;
            }

            // get point adjacent
            Point[] adjacentPoints = Arrays.stream(getAdjacent(current)).filter(p ->
                            (0 <= p.x && p.x < m) && (0 <= p.y && p.y <n)
                    ).toArray(Point[]::new);

            // loop through 2 adjacent
            for (Point adjPoint: adjacentPoints) {

                int x = adjPoint.x;
                int y = adjPoint.y;
                if (visited[x][y] == 1) {
                    continue;
                }
                // not check
                visited[x][y] = 1;

                Point isInQueue = null;

                // check point is in queue, and has shorter distance
                var newDistance = current.distance + grid[x][y];
                for (Point queuePoint : queue) {
                    if (queuePoint.x == x && queuePoint.y == y && queuePoint.distance > newDistance) {
                        isInQueue = queuePoint;
                        break;
                    }
                }

                if (isInQueue != null) {
                    queue.remove(isInQueue);
                }

                // prepare to add into queue
                adjPoint.distance = newDistance;
                addPointToQueue(adjPoint, queue, visited);
            }
        }

        return 100000;
    }

    private Point[] getAdjacent(Point p) {
        return new Point[] {
                new Point(p.x +1, p.y),
                new Point(p.x, p.y +1)
        };
    }

}
