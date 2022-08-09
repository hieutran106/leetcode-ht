import unittest
from playground.heap_demo import  build_max_heap

class MyTestCase(unittest.TestCase):

    def testCase1(self):
        input = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        output = build_max_heap(input)
        self.assertEqual(output, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def testCase2(self):
        input = [4, 10, 3, 5, 1]
        output = build_max_heap(input)
        self.assertEqual(output, [10, 5, 3, 4, 1])


if __name__ == '__main__':
    unittest.main()

