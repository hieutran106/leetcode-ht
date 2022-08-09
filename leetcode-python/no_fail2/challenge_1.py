import sys

# link: https://www.hackerrank.com/contests/nofail-2/challenges
def solution(my_input):
    for i in range(0, len(my_input), 2):
        line = my_input[i+1]
        solve_case(line)


def solve_case(line):
    numbers = list(map(int, line.split(' ')))
    total = sum(numbers)
    s = 0
    for number in numbers:
        s += number
        left = total - s
        if left % 2 == 0:
            print('Possible')
            return
    print('Impossible')


if __name__ == "__main__":
    # my_input = [line.rstrip().split() for line in sys.stdin.readlines()]
    my_input = """6
6
1 4 7 9001 2 150000
3
1 2 10
10
1024 1 16 32 1 999 123 321 9 15
30
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
9
8 1 10 22 75 121 4 73 335
4
8 1 10 22"""
    my_input = my_input.split("\n")
    my_input = my_input[1:]
    solution(my_input)
