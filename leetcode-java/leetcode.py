import sys
import os

if __name__ == "__main__":
    number = int(sys.argv[1])
    name = sys.argv[2]

    bucket_size = 200

    bucket_num = (number // bucket_size) * bucket_size
    # _20xx
    bucket_name = f"_{bucket_num // 100}xx"
    fullname = f"_{number}_{name}"
    cwd = os.getcwd()

    bucket_path = os.path.join(cwd, bucket_name)
    solution_file_path = os.path.join(cwd, "src/main/java", bucket_name, fullname, "Solution.java")
    test_file_path = os.path.join(cwd, "src/test/java", bucket_name, fullname, "SolutionTest.java")

    # early exit
    if os.path.exists(solution_file_path):
        print("Solution existed. Exit ...")
        sys.exit()

    solution_directory = os.path.dirname(solution_file_path)
    test_directory = os.path.dirname(test_file_path)
    os.makedirs(solution_directory, exist_ok=True)
    os.makedirs(test_directory, exist_ok=True)

    package_name = f"{bucket_name}.{fullname}"
    test_content = f"""package {package_name};

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class SolutionTest {{
    @Test
    public void testCase1() {{
        Assertions.assertEquals(1, 1);
    }}
}}
    """

    solution_content = f"""package {package_name};

public class Solution {{

}}
    """
    # create solution file
    with open(solution_file_path, 'w+') as f:
        f.writelines(solution_content)

    # create test file
    with open(test_file_path, 'w+') as f:
        f.writelines(test_content)