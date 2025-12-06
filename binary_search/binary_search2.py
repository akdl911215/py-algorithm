def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    step = 0

    while left <= right:
        step += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
idx = binary_search(arr, 9)
print("결과 인덱스:", idx)
