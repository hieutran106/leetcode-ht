from typing import List


class MaxHeap:
    """
    Priority queue is an abstract data type, which is a shorthand way of describing a particular interface and behavior,
    and says nothing about the underlying implementation.
    A heap is a good data structure to implement a priority queue.
    """
    def __init__(self, data=[], key=lambda x: x):
        self.key = key
        self.heap = self.build_heap(data)


    def build_heap(self, data):
        """
        Build heap from iterable
        :param data:
        :return:
        """
        heap = list.copy(data)
        # start from the last non-leaf node
        middle = len(data) // 2
        for i in reversed(range(middle)):
            self.sift_down(heap, i)
        return heap

    def sift_down(self, heap, start):
        """
        Sifting down operation moves the value successively down the tree if its children has bigger value.
        This is done to maintain the heap order.
        :param heap:
        :param start:
        :return:
        """
        while 2 * start + 1 < len(heap):
            largest = start
            left = 2 * start + 1
            right = 2 * start + 2
            if self.key(heap[left]) > self.key(heap[start]):
                largest = left

            if right < len(heap) and self.key(heap[right]) > self.key(heap[largest]):
                largest = right

            if largest == start:
                break

            # swap
            heap[start], heap[largest] = heap[largest], heap[start]
            start = largest

        return heap

    def sift_up(self, heap, start):
        """
        Move the value successively up the tree if its parent has smaller value
        :param heap:
        :param start:
        :return:
        """
        while (start - 1)//2 >= 0:
            parent = (start -1)//2
            if self.key(heap[parent]) >= self.key(heap[start]):
                break

            # swap
            heap[parent], heap[start] = heap[start], heap[parent]
            start = parent

        return heap


    def peek(self):
        """
        Get the top value of the heap.
        It returns the smallest value in min heap.
        TC O(1) | SC O(1)
        """
        return self.heap[0]

    def remove(self):
        """
        Remove maximum element from the heap
        It is important to ensure - TC O(logN) | SC O(1)
        :return:
        """
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")

        heap = self.heap
        heap[0], heap[-1] = heap[-1], heap[0]
        removed_value = heap.pop()
        self.sift_down(heap, 0)
        return removed_value

    def insert(self, value):
        """
        Insert an element to the heap
        Similar to heappush operation
        :param value:
        :return:
        """
        self.heap.append(value)
        self.sift_up(self.heap, len(self.heap) -1)