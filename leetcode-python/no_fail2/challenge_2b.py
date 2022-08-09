import sys
maxSize = sys.maxsize

def solution(lines):
    sum = 0
    min_u = maxSize
    min_v = maxSize
    for line in lines:
        print(line)
        numbers = list(map(int, line.split(' ')))
        sum = sum + numbers[2]
        if numbers[0] < min_u:
            min_u = numbers[0]

        if numbers[1] < min_v:
            min_v = numbers[1]



    print(sum, min_u * min_v)



if __name__ == "__main__":
    my_input = [line.rstrip() for line in sys.stdin.readlines()]
#     my_input = """1 1 4
# 1 3 2"""
#     my_input = my_input.split("\n")
    my_input = my_input[1:]
    solution(my_input)
