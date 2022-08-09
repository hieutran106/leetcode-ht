import sys

def CountTriangles(A):
    n = len(A);

    A.sort();

    count = 0;

    for i in range(n - 1, 0, -1):
        l = 0;
        r = i - 1;
        while (l < r):
            if (A[l] + A[r] > A[i]):

                # If it is possible with a[l], a[r]
                # and a[i] then it is also possible
                # with a[l + 1]..a[r-1], a[r] and a[i]
                count += r - l;

                # checking for more possible solutions
                r -= 1;

            else:

                # if not possible check for
                # higher values of arr[l]
                l += 1;
    print(count)
    # print("No of possible solutions: ", count);


if __name__ == "__main__":
    my_input = [line.rstrip() for line in sys.stdin.readlines()]
#     my_input = """1 1 4
# 1 3 2"""
#     my_input = my_input.split("\n")
#     my_input = my_input[1:]
    word = my_input[0]
    array = list(map(int, my_input[1].split(' ')))

    CountTriangles(array)
