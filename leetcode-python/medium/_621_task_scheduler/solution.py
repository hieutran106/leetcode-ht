from typing import List
from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = Counter(tasks)
        max_heap = [-f for f in freqs.values()]
        heapq.heapify(max_heap)

        queue = deque([]) # store [-cnt, time]

        time = 0
        while len(max_heap) or len(queue) > 0:
            # Look at the queue and see if we can put data to heap
            if len(queue) > 0:
                if queue[0][1] <= time:
                    top = queue.popleft()
                    heapq.heappush(max_heap, top[0])

            if len(max_heap) ==0:
                # idle
                # print("Must idle")
                time += 1
                continue

            # otherwise, can process a task
            # get the most frequent item from the heap
            cnt = 1 + heapq.heappop(max_heap)
            if cnt < 0 :
                queue.append((cnt, time + n + 1))
            time += 1
        return time

