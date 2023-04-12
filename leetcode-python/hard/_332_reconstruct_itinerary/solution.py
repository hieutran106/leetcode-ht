import collections
from typing import List
import heapq


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # initializing adjacency list
        adjacency_list = collections.defaultdict(list)
        for start, end in tickets:
            dest = adjacency_list[start]
            heapq.heappush(dest, end)
        print(adjacency_list)

        curr = "JFK"
        result = [curr]
        next_airports = adjacency_list[curr]
        while next_airports:
            curr = heapq.heappop(next_airports)
            result.append(curr)
            next_airports = adjacency_list[curr]

        return result

