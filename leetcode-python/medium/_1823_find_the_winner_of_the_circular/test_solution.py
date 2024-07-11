import unittest
import collections
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        Use a queue to simulate circular list
        """
        q = collections.deque()
        for i in range(1, n + 1):
            q.append(i)

        count = 1
        while len(q) > 1:
            if count == k:
                q.popleft()
                count = 1
            else:
                n = q.popleft()
                q.append(n)
                count += 1
        return q[0]

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.findTheWinner(n = 5, k = 2)
        self.assertEqual(actual, 3)
        
    def test_case_2(self):
        actual = self.s.findTheWinner(n = 6, k = 5)
        self.assertEqual(actual, 1)

if __name__ == '__main__':
    unittest.main()

