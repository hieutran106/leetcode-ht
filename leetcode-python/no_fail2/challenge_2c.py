import sys


def solve(numbers, k):
    prices = list(range(1, k+1))
    rest = list(filter(lambda x: x not in numbers, prices))
    print(rest)
    if len(rest) == 0:
        print(0)
        return
    elif len(rest) == 1:
        print(1/k)
        return
    elif len(rest) == 2:
        print(2/k)
        return

    # more than 3 elements left
    result = []
    for i in range(1, len(rest)):
        result.append(rest[i] - rest[i - 1])

    print(result)
    # count number of 1 in result
    count_number_1 = result.count(1)
    prob = (count_number_1 + 1) / k
    print(prob)

if __name__ == "__main__":
    # lines = [line.rstrip() for line in sys.stdin.readlines()]
    lines = """4 10
4 1 7 3""".split("\n")
    n_k = list(map(int, lines[0].split(' ')))
    k = n_k[1]
    numbers = list(map(int, lines[1].split(' ')))

    # print(numbers)
    # print(k)
    solve(numbers, k)