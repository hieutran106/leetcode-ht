import sys
import os


test_content = """import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()    

if __name__ == '__main__':
    unittest.main()

"""

solution_content = """class Solution:
    pass
"""

if __name__ == "__main__":
    difficulty = sys.argv[1]
    problem = sys.argv[2]

    cwd = os.getcwd()
    path = os.path.join(cwd, difficulty, problem)

    # early exit
    if os.path.exists(path):
        print("Solution existed. Exit ...")
        sys.exit()

    print(f'Create {difficulty}/{problem}')
    os.mkdir(path)
    # create __init__.py
    file = os.path.join(path, '__init__.py')
    open(file, 'a').close()

    # create solution.py
    file = os.path.join(path, 'solution.py')
    with open(file, 'w+') as f:
        f.writelines(solution_content)

    # create test_solution.py
    file = os.path.join(path, 'test_solution.py')
    with open(file, 'w+') as f:
        f.writelines(test_content)



