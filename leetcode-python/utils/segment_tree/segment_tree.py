from typing import List
import unittest
# Start implementation
from math import ceil, log2


def calculate_segment_tree_size(n: int):
    """
    Calculate the size of the segment tree

    Args:
        n (int): The size of the array/ The number of leaf nodes
    """
    height = ceil(log2(n))
    return 2 ** (height + 1) - 1


class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        tree_size = calculate_segment_tree_size(self.n)
        self.tree = [None] * tree_size
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums: List[int], node_index: int, left: int, right: int):
        if left == right:
            self.tree[node_index] = nums[left]
            return
        mid = (left + right) // 2
        self.build(nums, 2 * node_index + 1, left, mid)
        self.build(nums, 2 * node_index + 2, mid + 1, right)
        self.tree[node_index] = self.tree[2 * node_index + 1] + self.tree[2 * node_index + 2]

    def query(self, left: int, right: int) -> int:
        root_index = 0  # We start from root
        start, end = 0, self.n - 1  # Root cover range [0, n -1] inclusive
        return self.query_helper(root_index, start, end, left, right)

    def query_helper(self, node_index: int, start: int, end: int, left: int, right: int) -> int:
        # if query range contains node range
        if left <= start and end <= right:
            return self.tree[node_index]
        # if not overlapping
        if end < left or right < start:
            return 0  # return identity value, 0 for range sum
        # partially overlap
        mid = (start + end) // 2
        left_value = self.query_helper(2 * node_index + 1, start, mid, left, right)
        right_value = self.query_helper(2 * node_index + 2, mid + 1, end, left, right)
        return left_value + right_value

    def update(self, index: int, val: int):
        self.update_helper(0, 0, self.n - 1, index, val)

    def update_helper(self, node_index, start, end, index, val):
        """
        Recursively traverse down the tree, choosing the left or right child based on which range contains the index to be updated.
        Update the leaf node corresponding to the index.
        Propagate the change upwards by updating all parent nodes.
        """
        if start == end:
            print(f"Set value for leaf node {node_index=}, {start=}, {end=}")
            self.tree[node_index] = val
            return
        mid = (start + end) // 2
        if index <= mid:
            self.update_helper(2 * node_index + 1, start, mid, index, val)
        else:
            # do something on the right
            self.update_helper(2 * node_index + 2, mid + 1, end, index, val)
        self.tree[node_index] = self.tree[2 * node_index + 1] + self.tree[2 * node_index + 2]


class MyTestCase(unittest.TestCase):

    def test_case1(self):
        segment_tree = SegmentTree([3, 4, 10, 2, 7])
        internal_tree = segment_tree.tree
        self.assertEqual([26, 17, 9, 7, 10, 2, 7, 3, 4, None, None, None, None, None, None], internal_tree)

    def test_case2(self):
        segment_tree = SegmentTree([3, 4, 10, 2, 7])
        actual = segment_tree.query(0, 4)
        self.assertEqual(26, actual)

    def test_case3(self):
        segment_tree = SegmentTree([3, 4, 10, 2, 7])
        actual = segment_tree.query(1, 3)
        self.assertEqual(16, actual)

    def test_case4(self):
        segment_tree = SegmentTree([1, 2, 5, 6, 7, 9])
        actual = segment_tree.query(2, 4)
        self.assertEqual(18, actual)

    def test_case5(self):
        segment_tree = SegmentTree([1, 2, 5, 6, 7, 9])
        segment_tree.update(0, 1)
        internal_tree = segment_tree.tree
        self.assertEqual([29, 7, 22, 2, 5, 13, 9, 0, 2, None, None, 6, 7, None, None], internal_tree)

    def test_case6(self):
        segment_tree = SegmentTree([0, 2, 5, 6, 7, 9])
        internal_tree = segment_tree.tree
        self.assertEqual([29, 7, 22, 2, 5, 13, 9, 0, 2, None, None, 6, 7, None, None], internal_tree)


if __name__ == '__main__':
    unittest.main()
