def recursive_midpoint_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    low = min(arr)
    high = max(arr)

    # Base case for lists of identical values
    if low == high:
        return arr

    midpoint = (low + high) / 2

    left = [x for x in arr if x < midpoint]
    right = [x for x in arr if x >= midpoint]

    return recursive_midpoint_sort(left) + recursive_midpoint_sort(right)