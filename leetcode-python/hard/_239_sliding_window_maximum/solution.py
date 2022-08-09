from typing import List, Deque
from collections import deque

def add_item(queue: Deque[int], v: int):
    while len(queue) > 0 and v > queue[-1]:
        queue.pop()
    queue.append(v)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        result = []
        for i in range(0, len(nums) - k + 1):
            if i == 0:
                for j in range(k):
                    add_item(queue, nums[j])
            else:
                if len(queue) > 0 and  nums[i-1] == queue[0]:
                    queue.popleft()
                # add new item to queue
                added_value = nums[i + k - 1]
                add_item(queue, added_value)
            # print(f"At {i=}, window={nums[i: i+k]}, {queue=}")

            result.append(queue[0])
            # print(f"Append {queue[0]} to result, {result=}")
        return result
