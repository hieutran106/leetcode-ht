import unittest
from typing import List
from functools import cmp_to_key
#2025-08-06
def original(a: int, b: int):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

def compare(a: int, b: int) -> bool:
    s1 = len(str(a))
    s2 = len(str(b))
    pad = abs(s1-s2)
    if s1 < s2:
        return original(a * 10 ** pad, b)
    elif s1 > s2:
        return original(a, b * 10 ** pad)
    else:
        return original(a, b)

class Solution2:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [i for i in range(1, n + 1)]
        ans = sorted(nums, key = cmp_to_key(compare))
        return ans


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def dfs(num):
            if num > n: return
            ans.append(num)
            for d in range(0, 10):
                dfs(num * 10 + d)

        for i in range(1, 10):
            dfs(i)
        return ans
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.lexicalOrder(n = 13)
        self.assertEqual(actual, [1,10,11,12,13,2,3,4,5,6,7,8,9])

        
    def test_case_2(self):
        actual = self.s.lexicalOrder(n=2)
        self.assertEqual(actual, [1, 2])

    def test_case_3(self):
        self.assertEqual(1, compare(132, 124))

    def test_case_4(self):
        self.assertEqual(-1, compare(499, 5))

    def test_case_5(self):
        self.assertEqual(1, compare(9, 1234))



if __name__ == '__main__':
    unittest.main()

