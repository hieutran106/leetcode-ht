def Max_heapify(A, i):
    heapsize = len(A)
    l = 2 * i + 1
    r = 2 * i + 2
    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heapsize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        Max_heapify(A, largest)


def build_max_heap(A):
    for i in range(len(A)//2 -1, -1, -1):
        Max_heapify(A, i)

    return A


if __name__ == "__main__":
    input = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    output = build_max_heap(input)
    print(output)