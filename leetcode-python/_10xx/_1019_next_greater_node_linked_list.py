import unittest
from typing import List, Optional
from utils.my_list import createListFromArray, ListNode


#2025-02-04
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # using decreasing monotonic stack
        stack = []
        curr = head
        i = 0
        ans = []
        while curr is not None:
            ans.append(0)
            curr = curr.next
        curr = head

        while curr is not None:
            while stack and stack[-1][0] < curr.val:
                val, index = stack.pop()
                ans[index] = curr.val
            stack.append([curr.val, i])

            i+= 1
            curr = curr.next
        return ans
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        head = createListFromArray([2,1,5])
        actual = self.s.nextLargerNodes(head)
        self.assertEqual([5,5,0], actual)
        
    def test_case_2(self):
        head = createListFromArray([2,7,4,3,5])
        actual = self.s.nextLargerNodes(head)
        self.assertEqual([7,0,5,5,0], actual)

    def test_case_3(self):
        head = createListFromArray([2,7,4,3,5,8])
        actual = self.s.nextLargerNodes(head)
        self.assertEqual([7,8,5,5,8,0], actual)

if __name__ == '__main__':
    unittest.main()

