def search_insert(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

print(search_insert([1, 3, 5, 6], 5))
print(search_insert([1, 3, 5, 6], 2))
