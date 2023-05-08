import unittest
from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adjacency_matrix[i][j] = d
                adjacency_matrix[j][i] = d

        visited = set()
        min_heap = []
        cost = 0

        def add_edges_to_heap(node_idx):
            for i in range(n):
                if i == node_idx:
                    continue
                if i in visited:
                    continue
                heapq.heappush(min_heap, (adjacency_matrix[node_idx][i], node_idx, i))
            print(f"Add edges from node: {node_idx}")
            print(min_heap)
            visited.add(node_idx)

        # start at node 0
        add_edges_to_heap(0)

        while len(visited) < n:
            edge_cost, from_node, to_node = heapq.heappop(min_heap)
            if to_node in visited:
                continue
            cost += edge_cost
            print("=======================")
            print(f"Add edge [{from_node}, {to_node}]. Additional cost: {edge_cost}")
            print(f"Current cost: {cost}")
            add_edges_to_heap(to_node)
        return cost


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])
        self.assertEqual(20, actual)

    def test_case_2(self):
        actual = self.s.minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]])
        self.assertEqual(18, actual)


if __name__ == '__main__':
    unittest.main()
