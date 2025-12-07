def list_sum(arr):
    if len(arr) == 0:
        return 0

    az = arr[0]
    ls = list_sum(arr[1:])

    return az + ls

print(list_sum([1, 2, 3, 4]))  # 10