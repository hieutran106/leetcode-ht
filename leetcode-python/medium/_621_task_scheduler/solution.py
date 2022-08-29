from typing import List
from collections import Counter, deque
from queue import PriorityQueue


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = PriorityQueue()

        freqs = Counter(tasks).items()
        for key, value in freqs:
            heap.put((-value, key))

        queue = deque([])

        time = 0
        while not heap.empty() or len(queue) > 0:
            # print("====================")
            # print(f"Process at {time=}")
            # print(f"Current queue: {queue}")
            # Look at the queue and see if we can put data to heap
            if len(queue) > 0:
                if queue[0][1] <= time:
                    top = queue.popleft()
                    put_item = (top[0], top[2])
                    # print(f"Put item {put_item} to heap")
                    heap.put(put_item)

            if heap.empty():
                # idle
                # print("Must idle")
                time += 1
                continue

            # otherwise, can process a task
            f, task = heap.get()
            # print(f"Process task {task}")
            if f + 1 < 0 :
                item = (f + 1, time + n + 1, task)
                # print(f"Put element {item} to queue")
                queue.append(item)

            time += 1
        return time

