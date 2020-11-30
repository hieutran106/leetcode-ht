from utils.my_list import ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head

        while current is not None:
            next = current.next
            current.next = prev

            prev = current
            current = next

        return prev
