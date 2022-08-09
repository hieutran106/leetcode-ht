def fib_old(nth):
    if nth==1 or nth==2:
        return 1

    result = [1, 1]
    for i in range(2, nth):
        curr = result[i-1] + result[i-2]
        result.append(curr)

    return result[-1]


def fib(n: int):
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2

def solution(n: int , k: int):
    fib_n = fib(n)
    # result = fib_n % (10 ** k)
    fib_str = str(fib_n)
    return fib_str[-k:]

if __name__ == "__main__":
    input = input().split(" ")
    n = int(input[0])
    k = int(input[1])
    result = solution(n, k)
    print(result)

