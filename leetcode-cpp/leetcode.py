import sys
import os


test_content = """#include "../test/catch_amalgamated.hpp"

using namespace std;

class Solution
{
};

TEST_CASE("test_case_1")
{
    Solution s;
    CHECK(true);
}

TEST_CASE("test_case_2")
{
    Solution s;
    CHECK(true);
}

"""

solution_content = """class Solution:
    pass
"""

if __name__ == "__main__":
    number = int(sys.argv[1])
    name = sys.argv[2]

    bucket_size = 200

    bucket_num = (number // bucket_size) * bucket_size
    # _20xx
    bucket_name = f"_{bucket_num // 100}xx"
    filename = f"_{number}_{name}.cpp"
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

    # create solution file
    with open(solution_file_path, 'w+') as f:
        f.writelines(test_content)



