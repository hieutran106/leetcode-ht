import sys
import itertools

def solution(my_input):
    for i in range(0, len(my_input), 2):
        line = my_input[i+1]
        solve_case(line)


def solve_case(line):
    numbers = list(map(int, line.split(' ')))
    # check duplication
    set_numbers = set(numbers)
    if len(numbers) != len(set_numbers):
        print("Possible")
        return

    at_least = 3
    at_most = 4
    diff_len_max = len(set_numbers) - at_least
    diff_len_min = len(set_numbers) - at_most
    if diff_len_min < 0:
        diff_len_min = 0
    for i in range(diff_len_min, diff_len_max+1):
        to_be_removed = itertools.combinations(set_numbers, i)
        for removed_element in to_be_removed:
            rest = set_numbers - set(removed_element)
            rest = list(rest)
            # print(rest)
            result = canPartition(rest)
            if result:
                print("Possible")
                return
    print("Impossible")


def canPartition(nums):
	target, n = sum(nums), len(nums)
	if target & 1: return False
	target >>= 1
	dp = [True] + [False]*target
	for x in nums:
		dp = [dp[s] or (s >= x and dp[s-x]) for s in range(target+1)]
		if dp[target]: return True
	return False






if __name__ == "__main__":
    my_input = [line.rstrip()for line in sys.stdin.readlines()]
    my_input = my_input[1:]
    solution(my_input)
