import unittest

import utils.my_list
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        head = utils.my_list.createListFromArray([1, 2, 3, 4, 5])
        head_after = self.s.removeNthFromEnd(head, 2)

        self.assertEqual([1, 2, 3, 5], utils.my_list.createArrayFromList(head_after))

    def test_case_2(self):
        head = utils.my_list.createListFromArray([1])
        head_after = self.s.removeNthFromEnd(head, 1)

        self.assertEqual([], utils.my_list.createArrayFromList(head_after))

    def test_case_3(self):
        head = utils.my_list.createListFromArray([1, 2])
        head_after = self.s.removeNthFromEnd(head, 1)

        self.assertEqual([1], utils.my_list.createArrayFromList(head_after))

    def test_case_4(self):
        head = utils.my_list.createListFromArray([1, 2, 3, 4])
        head_after = self.s.removeNthFromEnd(head, 1)

        self.assertEqual([1, 2, 3], utils.my_list.createArrayFromList(head_after))

    def test_case_5(self):
        head = utils.my_list.createListFromArray([1, 2, 3, 4])
        head_after = self.s.removeNthFromEnd(head, 4)

        self.assertEqual([2, 3, 4], utils.my_list.createArrayFromList(head_after))

    def test_case_6(self):
        head = utils.my_list.createListFromArray([1, 2])
        head_after = self.s.removeNthFromEnd(head, 1)

        self.assertEqual([1], utils.my_list.createArrayFromList(head_after))

if __name__ == '__main__':
    unittest.main()

