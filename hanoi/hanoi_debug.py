def hanoi_debug(n: int, from_rod: str, to_rod: str, aux_rod: str, depth: int = 0):
    indent = "  " * depth
    print(f"{indent}hanoi(n={n}, from={from_rod}, to={to_rod}, aux={aux_rod}) 호출")

    if n == 1:
        print(f"{indent}=> 원판 1: {from_rod} -> {to_rod} (직접 이동)")
        return

    # 1) 위의 n-1개를 보조 막대로
    print(f"{indent}1단계: n-1개를 {from_rod} -> {aux_rod} 로 옮기기 (to={to_rod}는 보조 역할)")
    hanoi_debug(n - 1, from_rod, aux_rod, to_rod, depth + 1)

    # 2) 가장 큰 원판 1개를 목표 막대로
    print(f"{indent}2단계: 가장 큰 원판 {n}을 {from_rod} -> {to_rod} 로 옮기기")
    print(f"{indent}   이동: 원판 {n}: {from_rod} -> {to_rod}")

    # 3) 보조 막대에 있던 n-1개를 목표 막대로
    print(f"{indent}3단계: n-1개를 {aux_rod} -> {to_rod} 로 옮기기 (from={from_rod}는 보조 역할)")
    hanoi_debug(n - 1, aux_rod, to_rod, from_rod, depth + 1)


print("=== 하노이 n=3 디버그 ===")
hanoi_debug(3, "A", "C", "B")
