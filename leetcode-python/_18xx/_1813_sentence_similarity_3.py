import unittest
from typing import List

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        pass
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.areSentencesSimilar(sentence1 = "My name is Haley", sentence2 = "My Haley")
        self.assertEqual(True, actual)
        
    def test_case_2(self):
        actual = self.s.areSentencesSimilar(sentence1 = "of", sentence2 = "A lot of words")
        self.assertEqual(False, actual)

    def test_case_3(self):
        actual = self.s.areSentencesSimilar(sentence1 = "Eating right now", sentence2 = "Eating")
        self.assertEqual(True, actual)

if __name__ == '__main__':
    unittest.main()

