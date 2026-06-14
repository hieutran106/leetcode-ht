import unittest
from typing import List, Optional
from utils.my_list import createListFromArray, ListNode

# Date: 2026-06-14
# Problem: 2130 max_twin_sum_of_linked_list
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        my_list = []
        while (head):
            my_list.append(head.val)
            head = head.next
        n = len(my_list)
        ans = float("-inf")
        for i in range(n//2):
            ans = max(ans, my_list[i] + my_list[n-1-i])
        return ans
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        head = createListFromArray([5,4,2,1])
        actual = self.s.pairSum(head)
        self.assertEqual(actual, 6)
        
    def test_case_2(self):
        head = createListFromArray([4,2,2,3])
        actual = self.s.pairSum(head)
        self.assertEqual(actual, 7)

    def test_case_3(self):
        head = createListFromArray([1,100000])
        actual = self.s.pairSum(head)
        self.assertEqual(actual, 100001)

if __name__ == '__main__':
    unittest.main()

