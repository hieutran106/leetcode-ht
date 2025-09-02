#!/usr/bin/env python3

import re
import sys
import os
import glob
from pathlib import Path
from datetime import datetime

_pattern = re.compile(r'\{\s*([A-Za-z_][A-Za-z0-9_]*)\s*\}')

solution_template = """
#include <catch2/catch_test_macros.hpp>

// Date: {current_date}
// Problem: {problem_number} {problem_name}
using std::vector;
using std::string;

class Solution {

};

Solution s;
TEST_CASE("[{problem_number}] Test case 1", "") {
    REQUIRE(1 == 1);
}


TEST_CASE("[{problem_number}] Test case 2", "") {
    REQUIRE(1 == 1);
}

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

if __name__ == "__main__":
    number = int(sys.argv[1])
    name = sys.argv[2]

    bucket_size = 200

    bucket_num = (number // bucket_size) * bucket_size
    # _20xx
    bucket_name = f"_{bucket_num // 100}xx"
    problem_name = f"_{number}_{name}"
    filename = f"{problem_name}.cpp"
    cwd = os.getcwd()

    bucket_path = os.path.join(cwd, bucket_name)
    solution_file_path = os.path.join(cwd, bucket_name, filename)

    # early exit
    pattern = f"_{number}_*.cpp"
    path = Path(bucket_name)
    matching_files = list(path.glob(pattern))
    if matching_files:
        print("Solution existed. Exit ...")
        sys.exit()

    print(f'Create bucket folder {bucket_name}')
    os.makedirs(bucket_path, exist_ok=True)


    # create solution file
    with open(solution_file_path, 'w+') as f:
        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y-%m-%d")
        data = {
            "current_date": formatted_date,
            "problem_number": number,
            "problem_name": name
        }
        content = render(solution_template, data)
        f.writelines(content)

    # append executable to CMakeLists.txt file
    cmake_file_path = os.path.join(cwd, bucket_name, "CMakeLists.txt")
    with open(cmake_file_path, "a") as file:
        file.write("\n")
        file.write(f"add_executable({problem_name} {problem_name}.cpp)\n")
        file.write(f"target_link_libraries({problem_name} PRIVATE Catch2::Catch2WithMain)\n")

    # check if root-level CMakeLists.txt includes proper add_subdirectory
    with open("CMakeLists.txt", "r") as root_cmake_list:
        lines = root_cmake_list.readlines()

    add_subdirectory_str = f"add_subdirectory({bucket_name})"
    found = add_subdirectory_str in lines
    if not found:
        with open("CMakeLists.txt", "r+") as root_cmake_list:
            content = root_cmake_list.read()
            if not content.endswith("\n"):
                root_cmake_list.write("\n")
            root_cmake_list.write(f"{add_subdirectory_str}\n")
        print(f"{add_subdirectory_str} was not found in the root CMakeLists.txt and has been appended to the file")
    else:
        print(f"{add_subdirectory_str} already exists in the root CMakeLists.txt file")