import unittest

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        r = time % (2 *n -2)
        if r <n:
            return r + 1
        else:
            return -r + 2*n - 1

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.passThePillow(n = 4, time = 5)
        self.assertEqual(actual, 2)
        
    def test_case_2(self):
        actual = self.s.passThePillow(n = 3, time = 2)
        self.assertEqual(actual, 3)

    def test_case_3(self):
        actual = self.s.passThePillow(n = 2, time = 1)
        self.assertEqual(actual, 2)

    def test_case_4(self):
        actual = self.s.passThePillow(n = 2, time = 2)
        self.assertEqual(actual, 1)

    def test_case_5(self):
        actual = self.s.passThePillow(n=1000, time=1000)
        self.assertEqual(actual, 999)

if __name__ == '__main__':
    unittest.main()

