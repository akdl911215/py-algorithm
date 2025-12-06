def sum_recursive_debug(n: int, depth: int = 0) -> int:
    indent = "  " * depth  # 깊이에 따라 들여쓰기

    print(f"{indent}sum_recursive({n}) 호출")

    if n == 1:
        print(f"{indent}=> n이 1이므로 1 반환")
        return 1

    result = sum_recursive_debug(n - 1, depth + 1) + n
    print(f"{indent}sum_recursive({n - 1}) 까지 계산된 값 + {n} = {result} 반환")
    return result


print("최종 결과:", sum_recursive_debug(4))
