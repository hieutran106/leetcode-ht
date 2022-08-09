# tags: graph, dijkstra
from typing import List
from .helper import MaxHeap
from collections import defaultdict


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int,
    ) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            source = edges[i][0]
            destination = edges[i][1]
            prob = succProb[i]
            # undirected graph
            graph[source].append((destination, prob))
            graph[destination].append((source, prob))

        # init dijstra
        visited = set()
        # edge relaxation
        COST_TO_START = 1
        max_distance = {start: COST_TO_START}
        max_heap = MaxHeap()
        max_heap.push(start, COST_TO_START)

        while not max_heap.is_empty():
            (curr_node, cost) = max_heap.pop()
            if curr_node == end:
                return cost

            visited.add(curr_node)
            # loop through current node's adjacent
            for next_node, cost in graph.get(curr_node, ()):
                # skip if visited
                if next_node in visited:
                    continue

                # edge relaxation
                if next_node not in max_distance:
                    max_distance[next_node] = max_distance[curr_node] * cost
                else:
                    if max_distance[curr_node] * cost > max_distance[next_node]:
                        max_distance[next_node] = max_distance[curr_node] * cost

                # update max_heap
                max_heap.push(next_node, max_distance[next_node])


        return 0

