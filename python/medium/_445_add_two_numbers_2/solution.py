from utils.my_list import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse_linked_list(l1)
        l2 = self.reverse_linked_list(l2)

        r = 0
        prev = None

        while not (l1 is None and l2 is None and r == 0):
            new_sum, new_r = self.sum(l1, l2, r, prev)
            r = new_r
            prev = new_sum
            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        return prev

    def sum(self, l1: ListNode, l2: ListNode, r: int, prev: ListNode) -> (ListNode, int):
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0
        val = val1 + val2 + r

        node = ListNode(val % 10)

        # link up
        node.next = prev
        new_r = val // 10

        return (node, new_r)


    def reverse_linked_list(self, head: ListNode) -> ListNode:
        prev = None
        current = head

        while current is not None:
            next = current.next
            current.next = prev

            prev = current
            current = next

        return prev