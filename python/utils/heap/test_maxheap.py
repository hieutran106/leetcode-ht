import unittest
from .maxheap import MaxHeap


class MyTestCase(unittest.TestCase):
    def testCase1(self):
        input = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        max_heap = MaxHeap(data=input)
        output = max_heap.heap
        self.assertEqual(output, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def testCase2(self):
        input = [4, 10, 3, 5, 1]
        max_heap = MaxHeap(input)
        output = max_heap.heap
        self.assertEqual(output, [10, 5, 3, 4, 1])

    def testCase3(self):
        input = [7, 6, 5, 4, 3, 2, 1]
        max_heap = MaxHeap(input)
        output = max_heap.heap
        self.assertEqual(output, [7, 6, 5, 4, 3, 2, 1])


    def test_shift_down1(self):
        max_heap = MaxHeap()
        output = max_heap.sift_down([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17], 4)
        # swap 6 and 17
        self.assertEqual(output, [1, 3, 5, 4, 17, 13, 10, 9, 8, 15, 6], "Swap 6 and 17")

        output = max_heap.sift_down([1, 3, 5, 4, 17, 13, 10, 9, 8, 15, 6], 3)
        # swap 4 and 9
        self.assertEqual(output, [1, 3, 5, 9, 17, 13, 10, 4, 8, 15, 6], "Swap 4 and 9")

        output = max_heap.sift_down([1, 17, 13, 9, 15, 5, 10, 4, 8, 3, 6], 0)
        self.assertEqual(
            output,
            [17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1],
            "Swap 1 and 17, then swap 1 and 15, finally swap 1 and 6",
        )

    def test_shift_up(self):
        max_heap = MaxHeap()
        output = max_heap.sift_up([1], 0)
        self.assertEqual(output, [1])

        output = max_heap.sift_up([1, 2], 1)
        self.assertEqual(output, [2, 1])

        output = max_heap.sift_up([10, 5, 3, 2, 4, 15], 5)
        self.assertEqual(output, [15, 5, 10, 2, 4, 3])

    def test_insert1(self):
        input = [10, 5, 3, 2, 4]
        max_heap = MaxHeap(input)
        max_heap.insert(15)
        output = max_heap.heap
        self.assertEqual(output, [15, 5, 10, 2, 4, 3])

    def test_remove1(self):
        input = [4, 10, 3, 5, 1]
        max_heap = MaxHeap(input)
        val = max_heap.remove()
        output = max_heap.heap
        self.assertEqual(val, 10)
        self.assertEqual(output, [5, 4, 3, 1])

    def test_remove2(self):
        input = [4]
        max_heap = MaxHeap(input)
        val = max_heap.remove()
        output = max_heap.heap
        self.assertEqual(val, 4)
        self.assertEqual(output, [])
        self.assertRaises(IndexError, max_heap.remove)



if __name__ == "__main__":
    unittest.main()
