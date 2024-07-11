import unittest

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full_count = numBottles
        empty_count = 0
        ans = 0
        while full_count > 0:
            ans += full_count
            # drink all full bottle
            empty_count += full_count
            # exchange
            full_count = empty_count // numExchange
            empty_count = empty_count - (full_count * numExchange)

        return ans
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.numWaterBottles(numBottles = 9, numExchange = 3)
        self.assertEqual(actual, 13)
        
    def test_case_2(self):
        actual = self.s.numWaterBottles(numBottles = 15, numExchange = 4)
        self.assertEqual(actual, 19)

    def test_case_3(self):
        actual = self.s.numWaterBottles(numBottles = 1, numExchange = 2)
        self.assertEqual(actual, 1)

if __name__ == '__main__':
    unittest.main()

