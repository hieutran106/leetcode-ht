import unittest
from .solution import Codec

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Codec()

    def testCase1(self):
        input_str = "1,2,3"
        root = self.s.deserialize(input_str)
        serialized_tree = self.s.serialize(root)
        self.assertEqual(serialized_tree, input_str)

    def testCase2(self):
        input = "1,2,3,null,null,4,5"
        root = self.s.deserialize(input)
        serialized_tree = self.s.serialize(root)
        self.assertEqual(serialized_tree, input)

    def testCase3(self):
        input = ""
        root = self.s.deserialize(input)
        serialized_tree = self.s.serialize(root)
        self.assertEqual(serialized_tree, input)

    def testCase4(self):
        input = "1,2"
        root = self.s.deserialize(input)
        serialized_tree = self.s.serialize(root)
        self.assertEqual(serialized_tree, input)

if __name__ == '__main__':
    unittest.main()

