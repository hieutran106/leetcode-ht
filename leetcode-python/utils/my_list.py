from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"ListNode({self.val=}, {self.next=}"


def createListFromArray(arr: List) -> ListNode:
    if (len(arr) == 0):
        return None

    last = None
    for index, ele in reversed(list(enumerate(arr))):
        node = ListNode(ele, last)
        last = node
        if index == 0:
            return node


def createArrayFromList(head: ListNode) -> List[int]:
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next

    return result


def deserialize(data: str):
    n = len(data)
    if data.startswith('[') and data.endswith(']'):
        data = data[1:n - 1]
    ret = list(map(lambda x: int(x), data.split(',')))
    return ret
