#!/usr/bin/env python3

import re
import sys
import os
from datetime import datetime

_pattern = re.compile(r'\{\s*([A-Za-z_][A-Za-z0-9_]*)\s*\}')

solution_template = """import unittest
from typing import List

# Date: {current_date}
# Problem: {problem_number} {name}
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

def render(template: str, data: dict, missing: str = '') -> str:
    """
    Replace { name } with data['name'] for simple identifiers.
    If a key is missing, insert the value of `missing` (default: '').
    """
    def _repl(m):
        key = m.group(1)
        return str(data.get(key, missing))
    return _pattern.sub(_repl, template)

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
        data = {
            "current_date": formatted_date,
            "problem_number": number,
            "name": name
        }
        content = render(solution_template, data)
        f.writelines(content)



