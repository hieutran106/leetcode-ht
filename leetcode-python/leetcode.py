import re
import sys
import os
from datetime import datetime

test_content = """import unittest
from typing import List

# Date: {current_date}
class Solution:
    pass
    

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
    
    def test_case_1(self):
        pass
        
    def test_case_2(self):
        pass

if __name__ == '__main__':
    unittest.main()

"""

solution_content = """class Solution:
    pass
"""

def replace_pattern(text, replacement):
    pattern = r'\{.*?\}'
    return re.sub(pattern, replacement, text)

if __name__ == "__main__":
    number = int(sys.argv[1])
    name = sys.argv[2]

    bucket_size = 200

    bucket_num = (number // bucket_size) * bucket_size
    # _20xx
    bucket_name = f"_{bucket_num // 100}xx"
    filename = f"_{number}_{name}.py"
    cwd = os.getcwd()

    bucket_path = os.path.join(cwd, bucket_name)
    solution_file_path = os.path.join(cwd, bucket_name, filename)
    init_file_path = os.path.join(bucket_path, "__init__.py")
    # early exit
    if os.path.exists(solution_file_path):
        print("Solution existed. Exit ...")
        sys.exit()

    print(f'Create bucket folder {bucket_name}')
    os.makedirs(bucket_path, exist_ok=True)
    # create __init__.py if needed
    if not os.path.exists(init_file_path):
        open(init_file_path, 'a').close()

    # create solution file
    with open(solution_file_path, 'w+') as f:
        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y-%d-%m")
        new_test_content = replace_pattern(test_content, formatted_date)
        f.writelines(new_test_content)



