def subset_sum(arr, target, i=0):
    if target == 0:
        return True

    if i == len(arr):
        return False

    # Include current element
    if subset_sum(arr, target - arr[i], i + 1):
        return True

    # Exclude current element
    return subset_sum(arr, target, i + 1)

print(subset_sum([3, 4, 5, 2], 9))
print(subset_sum([1, 2, 3], 7))
