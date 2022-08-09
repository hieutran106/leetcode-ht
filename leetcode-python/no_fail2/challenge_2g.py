import collections
import sys
import heapq

def solve(m, source, rows, cols):
    visited = [[False] * cols for _ in range(rows)]

    q = [(0, source)]
    mins = {source: 0}
    sr = source[0]
    sc = source[1]
    visited[sr][sc] = True
    while q:
        cost, curr_cell = heapq.heappop(q)
        r = curr_cell[0]
        c = curr_cell[1]

        if m[r][c] == 'e':
            return cost

        # mark as visited
        visited[r][c] = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dir in directions:
            next_r = r + dir[0]
            next_col = c + dir[1]
            if next_r <0 or next_r >= rows:
                continue

            if next_col<0 or next_col >=cols:
                continue

            if visited[next_r][next_col]:
                continue
            if m[next_r][next_col] == '*':
                continue

            # otherwise consider add to queue
            prev = mins.get((next_r, next_col), None)
            next = cost + 1
            condition = prev is None or next < prev
            if condition:
                next_node = (next_r, next_col)
                mins[next_node] = next
                heapq.heappush(q, (next, next_node))

    return -1


def get_infos(lines):
    first_line = list(map(int, lines[0].split(" ")))
    rows = first_line[0]
    cols = first_line[1]

    matrix = lines[1:]
    source = None

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 's':
                source = (i, j)

    return matrix, source, rows, cols


if __name__ == "__main__":

#     lines = """4 5
# .....
# s...*
# *****
# .e*..""".split("\n")
    lines = [line.rstrip() for line in sys.stdin.readlines()]

    matrix, source, rows, cols = get_infos(lines)
    print(matrix)
    print(source)

    result = solve(matrix, source, rows, cols)
    if result != -1:
        print(result)
    else:
        print("IMPOSSIBLE")