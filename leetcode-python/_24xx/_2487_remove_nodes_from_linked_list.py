import unittest
from typing import List, Optional
from utils.my_list import createListFromArray, createArrayFromList, ListNode

#2025-04-04
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        curr = head
        stack = []
        while curr is not None:
            nums.append(curr.val)
            curr = curr.next
        for n in nums:
            while stack and stack[-1] < n:
                stack.pop()
            stack.append(n)

        ans = None
        while stack:
            node = ListNode(stack[-1], ans)
            ans = node
            stack.pop()
        return ans
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        head = createListFromArray([5,2,13,3,8])
        actual = self.s.removeNodes(head)
        self.assertEqual(createArrayFromList(actual), [13, 8])
        
    def test_case_2(self):
        head = createListFromArray([1,1,1,1])
        actual = self.s.removeNodes(head)
        self.assertEqual(createArrayFromList(actual), [1,1,1,1])

if __name__ == '__main__':
    unittest.main()

