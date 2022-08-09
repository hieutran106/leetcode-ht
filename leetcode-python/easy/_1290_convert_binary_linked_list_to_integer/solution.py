from utils.my_list import ListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        sum = 0
        while (head != None):
            sum = sum * 2 + head.val
            head = head.next

        return sum
