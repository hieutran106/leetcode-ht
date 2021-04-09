from collections import defaultdict
import heapq
import sys

def ferry_cost(edges, n):
    graph = defaultdict(list)
    for source, destination, fee in edges:
        graph[source].append((fee, destination))
        graph[destination].append((fee, source))

    visited = set()
    mins = {0: 0}
    q = [(0, 0)]
    while q:
        (cost, current_node) = heapq.heappop(q)
        if current_node not in visited:
            visited.add(current_node)
            if current_node == n - 1:
                return cost

            for c, next_node in graph.get(current_node, ()):
                if next_node in visited:
                    continue
                prev = mins.get(next_node, None)
                next = max(cost, c)
                condition = prev is None or next < prev
                if condition:
                    mins[next_node] = next
                    heapq.heappush(q, (next, next_node))


    return -1


if __name__ == '__main__':
    my_input = [line.rstrip() for line in sys.stdin.readlines()]

    n, m = list(map(int, my_input[0].split(" ")))
    edges = []
    for line in my_input[1:]:
        edge = [int(x) for x in line.split(" ")]
        edges.append(edge)


    result = ferry_cost(edges, n)
    print(result)