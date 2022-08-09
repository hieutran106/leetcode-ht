import sys
from typing import List
from utils.my_tree import TreeNode

class SegmentTreeNode(TreeNode):
    def __init__(self, value, left, right, low, high):
        super().__init__(value, left, right)
        self.low = low
        self.high = high

def get_sum(node: SegmentTreeNode, start: int, end: int) -> int:
    if node is None:
        raise ValueError(f"Node is None, start={start}, end={end}")
    if node.low >= start and node.high <= end:
        return node.val

    if node.high < start or node.low > end:
        return 0
    print(f"Process at node [val={node.val}]")
    left_value = get_sum(node.left, start, end)
    right_value = get_sum(node.right, start, end)
    return left_value + right_value


def build_segment_tree(arr: List[int], low, high) -> TreeNode:
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return SegmentTreeNode(arr[0],None, None, low, high)

    middle = len(arr) // 2
    middle_range = (high - low) // 2
    left = build_segment_tree(arr[:middle], low, middle_range)
    right = build_segment_tree(arr[middle:], middle_range, high)

    left_value = left.val if left is not None else 0
    right_value = right.val if right is not None else 0
    node = SegmentTreeNode(left_value + right_value, left, right, low, high)
    return node

def solution(reqs, array_a):
    result = []
    for line in reqs:
        req = list(map(int, line.split(" ")))
        if req[0] == 0:
            u, v = req[1:]
            total = sum(array_a[u:v+1])
            result.append(total)
        else:
            u, v, k = req[1:]
            for i in range(u, v + 1):
                array_a[i] += k

    return result



def main(input_lines: List[str]):
    input_array = [line.rstrip() for line in input_lines]
    n, m = list(map(int, input_array[0].split(" ")))
    array_a = list(map(int, input_array[1].split(" ")))
    result = solution(input_lines[2:], array_a)
    output = "\n".join(str(x) for x in result)
    return output

if __name__ == '__main__':
    input_lines = sys.stdin.readlines()
    output = main(input_lines)
    print(output)