import sys
import os
from pathlib import Path

if __name__ == "__main__":
    difficulty = sys.argv[1]
    problem = sys.argv[2]

    cwd = os.getcwd()
    path = os.path.join(cwd, "src", difficulty, problem)

    # early exit
    if os.path.exists(path):
        print("Solution existed. Exit ...")
        sys.exit()

    print(f'Create {difficulty}/{problem}')
    os.mkdir(path)
    # create solution.c
    file = os.path.join(path, 'solution.c')
    open(file, 'a').close()

    # create solution.h
    file = os.path.join(path, 'solution.h')
    open(file, 'a').close()

    # create test_solution.c
    file = os.path.join(path, 'test_solution.c')
    with open(file, 'w+') as f:
        test_solution_content = Path("templates/test_solution.c").read_text(encoding="utf-8")
        f.writelines(test_solution_content)

    # create Makefile
    file = os.path.join(path, 'Makefile')
    with open(file, 'w+') as f:
        makefile_content = Path("templates/Makefile").read_text(encoding="utf-8")
        result = makefile_content.replace("${problem_dir}", f"{difficulty}/{problem}")
        f.writelines(result)



