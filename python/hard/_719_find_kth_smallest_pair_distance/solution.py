from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        heap = []
        path = []
        self.backtrack(nums, 0, path, heap)
        heap.sort()
        return heap[k-1]

    def backtrack(self, nums: List[int], start, path, heap):
        if len(path) == 2:
            distance = abs(path[0] - path[1])
            heap.append(distance)
            return

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, i+1, path, heap)
            path.pop()
