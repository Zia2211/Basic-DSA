def floor_ceil(arr, target):
    floor_value = None
    ceil_value = None

    for num in arr:
        if num <= target:
            floor_value = num

        if num >= target:
            ceil_value = num
            break

    return floor_value, ceil_value

print(floor_ceil([1, 2, 4, 6, 8, 10], 5))
