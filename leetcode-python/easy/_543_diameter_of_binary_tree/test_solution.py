import unittest
from .solution import Solution
from utils.my_tree import deserialize, serialize


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        root = deserialize("1,2,3,4,5")
        actual = self.s.diameterOfBinaryTree(root)
        self.assertEqual(3, actual)

    def test_case_2(self):
        root = deserialize("1,2")
        actual = self.s.diameterOfBinaryTree(root)
        self.assertEqual(1, actual)

    def test_case_3(self):
        root = deserialize("1")
        actual = self.s.diameterOfBinaryTree(root)
        self.assertEqual(0, actual)

    def test_case_4(self):
        original_data = "1,2,3,4,5,null,null,null,6,null,7"
        root = deserialize(original_data)

        data = serialize(root)
        self.assertEqual(original_data, data)
        actual = self.s.diameterOfBinaryTree(root)
        self.assertEqual(4, actual)

    def test_case_5(self):
        original_data = "1,2,3,4,5,null,null,6,null,null,7,8,null,null,9"
        root = deserialize(original_data)

        data = serialize(root)
        self.assertEqual(original_data, data)
        actual = self.s.diameterOfBinaryTree(root)
        self.assertEqual(6, actual)


if __name__ == '__main__':
    unittest.main()
