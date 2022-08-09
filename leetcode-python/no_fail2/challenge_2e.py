from collections import defaultdict
import sys
import heapq
import itertools

def bfs(graph, start, end):

    q = [(0, start)]
    visited = set()
    visited.add(start)

    while q:
        (cost, current_node) = heapq.heappop(q)
        if current_node == end:
            return cost

        visited.add(current_node)
        for c, next_node in graph.get(current_node, ()):
            if next_node in visited:
                continue

            if cost == 0:
                next = c
            else:
                next = min(c, cost)
            heapq.heappush(q, (next, next_node))



def get_info(lines):
    n = int(lines[0])
    lines = lines[1:]
    edges = []
    sum = 0
    # build graph
    graph = defaultdict(list)
    for line in lines:
        source, destination, fee = list(map(int, line.split(' ')))

        result = None
        if source < destination:
            result = (source, destination)
        else:
            result = (destination, source)

        edges.append(result)
        sum = sum + fee
        graph[source].append((fee, destination))
        graph[destination].append((fee, source))

    return graph, n, edges, sum

def solve(graph, n, edges, sum):
    combinations = list(itertools.combinations(range(1, n + 1), 2))
    rest = list(filter(lambda x: x not in edges, combinations))
    for element in rest:
        value = bfs(graph, element[0], element[1])

        # add element to graph
        source = element[0]
        destination = element[1]
        fee = value
        # graph[source].append((fee, destination))
        # graph[destination].append((fee, source))
        print(f"value for new link ({source} {destination} - {fee})")

        sum = sum + value

    print(sum)
    return sum


if __name__ == "__main__":
    lines = [line.rstrip() for line in sys.stdin.readlines()]

#     lines =  """4
# 1 2 2
# 1 3 5
# 4 3 3""".split("\n")


    graph, n, edges, sum = get_info(lines)
    solve(graph, n, edges, sum)
