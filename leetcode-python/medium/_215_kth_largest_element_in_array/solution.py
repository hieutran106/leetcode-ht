# tags: max heap
from typing import List
from utils.heap.maxheap import MaxHeap

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = MaxHeap(nums)
        for i in range(k):
            result = max_heap.remove()

        return result