def flatten_debug(arr, depth=0):
    indent = "  " * depth
    print(f"{indent}flatten({arr}) 호출")

    result = []

    for item in arr:
        if isinstance(item, list):
            print(f"{indent}→ {item} 은 리스트 → 재귀 호출")
            result.extend(flatten_debug(item, depth + 1))
        else:
            print(f"{indent}→ {item} 추가")
            result.append(item)

    print(f"{indent}flatten({arr}) 결과 = {result}")
    return result


flatten_debug([1, [2, [3, 4], 5], 6])
