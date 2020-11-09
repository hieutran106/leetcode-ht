from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createListFromArray(arr: List) -> ListNode:
    if (len(arr) == 0):
        return None

    last = None
    for index, ele in reversed(list(enumerate(arr))):
        node = ListNode(ele, last)
        last = node
        if index == 0:
            return node
