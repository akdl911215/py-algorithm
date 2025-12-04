# 정수를 2진수 문자열로 보는 기본 함수
n = 13
print("10진수:", n)
print("2진수:", bin(n))  # 0b1101

# 비트 AND, OR, XOR, NOT, SHIFT
a = 0b1101  # 13
b = 0b1010  # 10

print("a & b:", bin(a & b))  # 둘 다 1일 때만 1
print("a | b:", bin(a | b))  # 하나라도 1이면 1
print("a ^ b:", bin(a ^ b))  # 다를 때만 1
print("a << 1:", bin(a << 1))  # 왼쪽으로 1비트 이동 == * 2
print("a >> 1:", bin(a >> 1))  # 오른쪽으로 1비트 이동 == // 2
