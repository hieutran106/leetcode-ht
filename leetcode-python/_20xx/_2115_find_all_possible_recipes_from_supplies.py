import unittest
from typing import List

#2025-21-03
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {}
        for i, r in enumerate(recipes):
            graph[r] = ingredients[i]

        can_cooked = set(supplies)
        visit = set()
        def dfs(r: str) -> bool:
            if r in can_cooked:
                return True
            if r not in graph or r in visit:
                return False

            visit.add(r)
            for ingredient in graph[r]:
                if not dfs(ingredient):
                    return False
            can_cooked.add(r)
            return True

        ans = []
        for r in recipes:
            if dfs(r):
                ans.append(r)

        return ans
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        actual = self.s.findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"])
        self.assertEqual(["bread"], actual)
        
    def test_case_2(self):
        actual = self.s.findAllRecipes(recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"])
        self.assertEqual(["bread","sandwich"], actual)

    def test_case_3(self):
        actual = self.s.findAllRecipes(recipes = ["bread","sandwich","burger"],
                                       ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]],
                                       supplies = ["yeast","flour","meat"])
        self.assertEqual(["bread","sandwich","burger"], actual)


    def test_case_4(self):
        actual = self.s.findAllRecipes(recipes = ["B","A","C"],
                                       ingredients = [["D","E"],["B","F"],["B","G"]],
                                       supplies = ["D","E","F"])
        self.assertEqual(["B","A"], actual) # No G supplies

    def test_case_5(self):
        actual = self.s.findAllRecipes(recipes=["ju","fzjnm","x","e","zpmcz","h","q"],
                                       ingredients=[
                                           ["d"],
                                           ["hveml","f","cpivl"],
                                           ["cpivl","zpmcz","h","e","fzjnm","ju"],
                                           ["cpivl","hveml","zpmcz","ju","h"],
                                           ["h","fzjnm","e","q","x"],
                                           ["d","hveml","cpivl","q","zpmcz","ju","e","x"],
                                           ["f","hveml","cpivl"]
                                       ],
                                       supplies=["f","hveml","cpivl","d"])
        self.assertEqual(["ju", "fzjnm", "q"], actual)  # No G supplies

    def test_case_6(self):
        actual = self.s.findAllRecipes(recipes=["burger","bread","sandwich"],
                                       ingredients=[["sandwich","meat","bread"],["yeast","flour"],["bread","meat"]],
                                       supplies=["yeast","flour","meat"])
        self.assertEqual(["burger","bread","sandwich"], actual)  # No G supplies
if __name__ == '__main__':
    unittest.main()

