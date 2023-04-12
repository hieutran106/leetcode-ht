import unittest
from .solution import Solution, Node

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()


    def test_case_1(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n1.neighbors = [n2, n4]
        n2.neighbors = [n1, n3]
        n3.neighbors = [n2, n4]
        n4.neighbors = [n1, n3]

        new_node = self.s.cloneGraph(n1)
        self.assertEqual(1, new_node.val)
        self.assertEqual(2, new_node.neighbors[0].val)
        self.assertEqual(4, new_node.neighbors[1].val)

    def test_case_2(self):
        n1 = Node(1)
        new_node = self.s.cloneGraph(n1)
        self.assertEqual(1, new_node.val)


if __name__ == '__main__':
    unittest.main()

