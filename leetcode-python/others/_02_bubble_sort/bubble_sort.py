def bubble_sort(nums):
    n = len(nums)

    # repeat n-1 times
    for i in range(0, n -1):
        swap = False
        for j in range(0, n - 1 - i):
            if nums[j] > nums[j+1]:
                # swap
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp
                swap = True
        if swap is not True:
            # early return
            return nums

    return nums


