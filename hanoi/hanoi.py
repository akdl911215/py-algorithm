import time
import os

def clear():
    """콘솔 화면 지우기 (원하면 주석 처리해도 됨)"""
    # 윈도우면 'cls', 맥/리눅스면 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')


def print_towers(state, n):
    """
    state: {'A': [큰원판..작은원판], ...}
    n: 전체 원판 개수
    """
    rods = ['A', 'B', 'C']
    max_width = 2 * n - 1

    # 각 막대마다 높이 n짜리 그리드 준비 (0은 비어 있음)
    grid = {rod: [0] * n for rod in rods}
    for rod in rods:
        stack = state[rod]
        # stack[0] = 맨 아래, stack[-1] = 맨 위
        for idx, size in enumerate(stack):
            grid[rod][idx] = size

    # 위에서부터 한 줄씩 출력 (level: 위쪽 → 아래쪽)
    for level in range(n - 1, -1, -1):
        line = ""
        for rod in rods:
            size = grid[rod][level]
            if size == 0:
                disc_str = "|"          # 빈 자리
            else:
                disc_str = "#" * (2 * size - 1)  # 원판 너비
            line += disc_str.center(max_width) + "   "
        print(line)

    # 바닥 + 라벨
    base = "=" * max_width
    print(f"{base}   {base}   {base}")
    print("A".center(max_width) + "   " +
          "B".center(max_width) + "   " +
          "C".center(max_width))
    print()  # 한 줄 띄우기


def hanoi(n, from_rod, to_rod, aux_rod, state, total_discs, delay=0.5, depth=0):
    """
    n: 옮길 원판 개수
    from_rod: 시작 기둥
    to_rod: 도착 기둥
    aux_rod: 보조 기둥
    state: 현재 각 기둥 상태
    total_discs: 전체 원판 개수 (시각화용)
    delay: 각 단계 사이 딜레이(초)
    depth: 디버깅용 깊이 (안 써도 됨)
    """
    if n == 1:
        # 가장 위에 있는 원판 하나를 실제로 옮김
        disc = state[from_rod].pop()   # from_rod의 맨 위 원판
        state[to_rod].append(disc)     # to_rod의 맨 위로 올림

        clear()
        print(f"원판 {disc}: {from_rod} -> {to_rod}")
        print_towers(state, total_discs)
        time.sleep(delay)
        return

    # 1) 위의 n-1개를 보조 기둥으로 옮기기
    hanoi(n - 1, from_rod, aux_rod, to_rod, state, total_discs, delay, depth + 1)

    # 2) 가장 큰 원판 1개를 목표 기둥으로 옮기기
    hanoi(1, from_rod, to_rod, aux_rod, state, total_discs, delay, depth + 1)

    # 3) 보조 기둥에 있는 n-1개를 목표 기둥으로 옮기기
    hanoi(n - 1, aux_rod, to_rod, from_rod, state, total_discs, delay, depth + 1)


if __name__ == "__main__":
    n = 3  # 원판 개수 바꿔보면서 테스트 가능 (예: 3, 4, 5)
    state = {
        'A': list(range(n, 0, -1)),  # [n, n-1, ..., 1] (아래에서 위 순서)
        'B': [],
        'C': []
    }

    clear()
    print("초기 상태")
    print_towers(state, n)
    time.sleep(1)

    hanoi(n, 'A', 'C', 'B', state, n, delay=0.7)
    print("완료!")
