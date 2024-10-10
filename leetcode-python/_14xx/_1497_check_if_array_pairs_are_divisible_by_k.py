import unittest
from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainders = [0] * k
        for num in arr:
            remainders[num % k] += 1
        for i in range(1, len(remainders)):
            if remainders[i] != remainders[k-i]:
                return False
        return True

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.canArrange(arr = [1,2,3,4,5,10,6,7,8,9], k = 5)
        self.assertEqual(True, actual)
        
    def test_case_2(self):
        actual = self.s.canArrange(arr = [1,2,3,4,5,6], k = 7)
        self.assertEqual(True, actual)

    def test_case_3(self):
        actual = self.s.canArrange(arr = [1,2,3,4,5,6], k = 10)
        self.assertEqual(False, actual)

    def test_case_4(self):
        actual = self.s.canArrange(arr = [-5, 10], k = 5)
        self.assertEqual(True, actual)

    def test_case_5(self):
        actual = self.s.canArrange(arr = [-5, 10, 4, 2], k = 5)
        self.assertEqual(False, actual)

    def test_case_6(self):
        actual = self.s.canArrange(arr = [-6, 5, 2, 1], k = 2)
        self.assertEqual(True, actual)

if __name__ == '__main__':
    unittest.main()

