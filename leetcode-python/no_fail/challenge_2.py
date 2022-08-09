import sys


def parse_input_submit(input_str):
    lines = input_str
    grid = []
    for line in lines[1:]:
        numbers = list(line)[0]
        x = list(map(lambda x: 1 if x == "1" else 0, numbers) )
        grid.append(x)
    return grid


def parse_input(input_str):
    lines = input_str.split("\n")
    grid = []
    for line in lines[1:]:
        numbers = list(line)
        x = list(map(lambda x: 1 if x == "1" else 0, numbers) )
        grid.append(x)
    return grid


def solution(grid):
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):

            if grid[i][j] == 1:
                count = max(dfs(i, j, grid), count)

    return count


def dfs(i, j, grid):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
        return 0

    grid[i][j] = 0

    up = dfs(i, j + 1, grid)
    down = dfs(i, j - 1, grid)
    left = dfs(i - 1, j, grid)
    right = dfs(i + 1, j, grid)

    return up + down + left + right + 1


if __name__ == "__main__":
    my_input = [line.rstrip().split() for line in sys.stdin.readlines()]
    grid = parse_input(my_input)
    result = solution(grid)
    print(result)
