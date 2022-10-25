from typing import Optional

from utils.my_list import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # go n step from head
        fast = head
        for _ in range(n):
            fast = fast.next

        if not fast:
            # we remove head node
            return head.next
        else:
            print(f"Fast node: {fast.val}")

        # find the node before n-th from end
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next

        print(f"Fast node: {fast.val}")
        print(f"Slow node: {slow.val}")
        # break linkage
        to_be_remove = slow.next
        slow.next = to_be_remove.next
        to_be_remove.next = None

        return head



