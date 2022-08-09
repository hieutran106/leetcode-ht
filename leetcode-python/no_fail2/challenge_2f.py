import sys

def solution(lines):
    first = 'T'
    for line in lines:
        num = int(line)
        if num % 4 == 0:
            # 2nd won
            won = 'Q' if first == 'T' else 'T'
        else:
            # 1st won
            won = 'Q' if first == 'Q' else 'T'

        if won == 'Q':
            print("Quang won!")
        else:
            print("Thien won!")

        # flip
        first = 'T' if won == 'Q' else 'Q'








if __name__ == "__main__":
    my_input = [line.rstrip() for line in sys.stdin.readlines()]
#     my_input = """1 1 4
# 1 3 2"""
#     my_input = my_input.split("\n")
#     my_input = my_input[1:]
#     my_input = """10
# 12
# 11
# 11
# 2
# 10
# 16
# 18
# 6
# 4
# 20"""
#     my_input = my_input.split("\n")
    my_input = my_input[1:]
    print(my_input)
    solution(my_input)