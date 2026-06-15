import unittest
from typing import List, Optional
from utils.my_list import createArrayFromList, createListFromArray, ListNode

# Date: 2026-06-16
# Problem: 2095 delete_middle_node_of_linked_list

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def middle(head: ListNode) -> ListNode:
            curr = head
            fast = curr.next

            while fast and fast.next and fast.next.next:
                curr = curr.next
                fast = fast.next.next

            return curr
        if head.next is None:
            return None
        mid = middle(head)
        print(f"Mid node is {mid.val}")


        mid.next = mid.next.next
        return head
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        head = createListFromArray([1,3,4,7,1,2,6])
        ans = self.s.deleteMiddle(head)
        actual = createArrayFromList(ans)
        self.assertEqual(actual, [1,3,4,1,2,6])

        
    def test_case_2(self):
        head = createListFromArray([1,2,3,4])
        ans = self.s.deleteMiddle(head)
        actual = createArrayFromList(ans)
        self.assertEqual(actual, [1, 2, 4])

    def test_case_3(self):
        head = createListFromArray([2, 1])
        ans = self.s.deleteMiddle(head)
        actual = createArrayFromList(ans)
        self.assertEqual(actual, [2])

    def test_case_4(self):
        head = createListFromArray([1])
        ans = self.s.deleteMiddle(head)
        actual = createArrayFromList(ans)
        self.assertEqual(actual, [])

if __name__ == '__main__':
    unittest.main()

