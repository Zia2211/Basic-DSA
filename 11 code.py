def first_last(arr, target):
    first = -1
    last = -1

    for i in range(len(arr)):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i

    return first, last

print(first_last([1, 2, 3, 2, 2, 4], 2))
