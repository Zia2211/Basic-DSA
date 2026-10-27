def lower_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def upper_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


def count_occurrences(arr, target):
    return upper_bound(arr, target) - lower_bound(arr, target)

print(count_occurrences([1, 2, 2, 2, 3, 4], 2))
