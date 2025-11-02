import unittest
from typing import List, Optional
from utils.my_list import ListNode, createListFromArray, createArrayFromList
# Date: 2025-11-01
# Problem: 3217 delete_nodes_from_linked_list
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        ans_head, ans_tail  = None, None
        while head:
            if head.val not in nums:
                new_node = ListNode(head.val)
                if not ans_head:
                    ans_head = new_node
                    ans_tail = new_node
                else:
                    ans_tail.next = new_node
                    ans_tail = new_node

            head = head.next

        return ans_head

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        head = createListFromArray([1,2,3,4,5])
        actual = self.s.modifiedList([1,2,3], head)
        actual_arr = createArrayFromList(actual)
        self.assertEqual(actual_arr, [4, 5])
        
    def test_case_2(self):
        head = createListFromArray([1,2,1,2,1,2])
        actual = self.s.modifiedList([1], head)
        actual_arr = createArrayFromList(actual)
        self.assertEqual(actual_arr, [2, 2, 2])

    def test_case_3(self):
        head = createListFromArray([1, 2, 3, 4])
        actual = self.s.modifiedList([5], head)
        actual_arr = createArrayFromList(actual)
        self.assertEqual(actual_arr, [1, 2, 3, 4])

    def test_case_4(self):
        head = createListFromArray([1, 1, 1, 1])
        actual = self.s.modifiedList([1], head)
        self.assertEqual(actual, None)

if __name__ == '__main__':
    unittest.main()

