import sys
import os

if __name__ == "__main__":
    difficulty = sys.argv[1]
    problem = sys.argv[2]

    cwd = os.getcwd()
    path = os.path.join(cwd, "src", "test", "java", difficulty, problem)

    # early exit
    if os.path.exists(path):
        print("Solution existed. Exit ...")
        sys.exit()

    print(f'Create {difficulty}/{problem}')
    os.mkdir(path)

    # create README.md
    file = os.path.join(path, 'README.md')
    open(file, 'a').close()

    # create SolutionTest.java
    file = os.path.join(path, 'SolutionTest.java')
    with open(file, 'w+') as f:
        test_content = f"""package {difficulty}.{problem};
import org.junit.Assert;
import org.junit.Test;

public class SolutionTest {{
    public static class Solution {{

    }}

    @Test
    public void testCase1() {{
        var s = new Solution();
    }}

    @Test
    public void testCase0() {{
        var s = new Solution();
    }}
}}"""
        f.writelines(test_content)



