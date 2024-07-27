import unittest
from typing import List

import collections
import heapq


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def createAdjacencyList():
            # Create graph represented as an adjacency list
            # graph = {
            #     'A': { 'B': 1, 'C': 3},
            #     'B': {'A': 1, 'D': 2, 'E': 3},
            # }
            graph = collections.defaultdict(dict)
            for source, target, distance in edges:
                graph[source][target] = distance
                graph[target][source] = distance

            return graph

        def dijkstra(start, graph):
            # Step 1: Initialize the distance dictionary with infinite distance for all nodes except the start node
            distances = {node: float('infinity') for node in range(n)}
            distances[start] = 0

            queue = [(0, start)]  # (distance, node)[]
            while queue:
                curr_distance, curr_node = heapq.heappop(queue)
                # Skip if this node has been processed already (implicit visited nodes
                if curr_distance > distances[curr_node]:
                    continue
                for neighbor, weight in graph[curr_node].items():
                    distance = curr_distance + weight

                    # Only update if new path is shorter
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(queue, (distance, neighbor))
            return distances

        graph = createAdjacencyList()

        ans = -1
        min_neighbor = float("infinity")
        for i in range(n):
            print(f"-----city={i}--")
            paths = dijkstra(i, graph)
            print(paths)
            count = 0
            for destination, d in paths.items():
                if 0 < d <= distanceThreshold:
                    count += 1
            if True or count > 0:
                print(f"{count=}")
                if count <= min_neighbor:
                    min_neighbor = count
                    ans = i
            print("========")
        return ans


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.findTheCity(n=4, edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold=4)
        self.assertEqual(actual, 3)

    def test_case_2(self):
        actual = self.s.findTheCity(n=5, edges=[[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]],
                                    distanceThreshold=2)
        self.assertEqual(actual, 0)

    def test_case_3(self):
        actual = self.s.findTheCity(n=6, edges=[[0, 3, 7], [2, 4, 1], [0, 1, 5], [2, 3, 10], [1, 3, 6], [1, 2, 1]],
                                    distanceThreshold=417)
        self.assertEqual(actual, 5)


if __name__ == '__main__':
    unittest.main()
