package medium._1584_min_cost_connect_all_points;

import org.junit.Assert;
import org.junit.Test;

import java.util.Comparator;
import java.util.HashSet;
import java.util.PriorityQueue;

public class SolutionTest {
    public class Solution {
        class Edge {
            int cost;
            int node;

            public Edge(int cost, int node) {
                this.cost = cost;
                this.node = node;
            }
        }

        public int minCostConnectPoints(int[][] points) {
            PriorityQueue<Edge> queue = new PriorityQueue<>(Comparator.comparingInt((Edge e) -> e.cost));
            queue.offer(new Edge(0, 0));

            HashSet<Integer> visited = new HashSet<>();
            int cost = 0;
            int len = points.length;

            while (visited.size() < len) {
                var edge = queue.poll();
                var currNode = edge.node;
                if (visited.contains(currNode)) {
                    continue;
                }
                visited.add(currNode);
                cost += edge.cost;

                for (int nextNode = 0; nextNode < points.length; nextNode++) {
                    if (visited.contains(nextNode)) {
                        continue;
                    }
                    int nextCost = Math.abs(points[nextNode][0] - points[currNode][0]) + Math.abs(points[nextNode][1] - points[currNode][1]);
                    Edge nextEdge = new Edge(nextCost, nextNode);
                    queue.offer(nextEdge);
                }
            }

            return cost;
        }


    }

    @Test
    public void testCase1() {
        int[][] points = {{0,0},{2,2},{3,10},{5,2},{7,0}};
        int actual = new Solution().minCostConnectPoints(
                points
        );
        Assert.assertEquals(20 , actual);
    }

    @Test
    public void testCase2() {
        int[][] points = {{3,12},{2,5},{-4,1}};
        int actual = new Solution().minCostConnectPoints(
                points
        );
        Assert.assertEquals(18 , actual);
    }

}
