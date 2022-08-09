from easy._1539_kth_missing_positive_number.solution import Solution
import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        actual = s.findKthPositive([1, 2, 3, 4], 2)
        self.assertEqual(actual, 6)