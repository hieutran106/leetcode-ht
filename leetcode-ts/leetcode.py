import sys
import os


test_content = """import { expect, test, describe } from "vitest";

describe("solution test", () => {
    test("test case 1", () => {
        expect(true).toBe(true);
    });

    test("test case 2", () => {
        expect(1 + 2).toBe(3);
    });
});

"""

if __name__ == "__main__":
    number = int(sys.argv[1])
    name = sys.argv[2]

    bucket_size = 200

    bucket_num = (number // bucket_size) * bucket_size
    # _20xx
    bucket_name = f"_{bucket_num // 100}xx"
    filename = f"_{number}_{name}.test.ts"
    cwd = os.getcwd()

    bucket_path = os.path.join(cwd, "src", bucket_name)
    solution_file_path = os.path.join(bucket_path, filename)

    # early exit
    if os.path.exists(solution_file_path):
        print("Solution existed. Exit ...")
        sys.exit()

    print(f'Create bucket folder {bucket_name}')
    os.makedirs(bucket_path, exist_ok=True)

    # create solution file
    with open(solution_file_path, 'w+') as f:
        f.writelines(test_content)



