import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.findMedianSortedArrays(nums1=[1, 3], nums2=[2])
        self.assertEqual(2, actual)

    def test_case_2(self):
        actual = self.s.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4])
        self.assertEqual(2.5, actual)

    def test_case_3(self):
        actual = self.s.findMedianSortedArrays(nums1=[1, 3, 5], nums2=[4, 6])
        self.assertEqual(4, actual)

    def test_case_4(self):
        actual = self.s.findMedianSortedArrays(nums1=[1, 3, 5], nums2=[])
        self.assertEqual(3, actual)

    def test_case_5(self):
        actual = self.s.findMedianSortedArrays(nums1=[], nums2=[1, 3, 5])
        self.assertEqual(3, actual)


if __name__ == '__main__':
    unittest.main()
