from utils.my_list import ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        # process each list node until the end
        while curr:
            # store next node to a temporary variable
            temp = curr.next
            # point back to previous node
            curr.next = prev
            # then move forward
            prev = curr
            curr = temp
        return prev



