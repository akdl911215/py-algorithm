def precedence(op):
    if op in ('+', '-'): return 1
    if op in ('*', '/'): return 2
    return 0

def apply_op(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

def evaluate(expression):
    nums = []
    ops = []
    i = 0

    while i < len(expression):
        ch = expression[i]

        # 공백은 건너뛰기
        if ch == ' ':
            i += 1
            continue

        # 숫자(다자리 지원)
        if ch.isdigit():
            val = 0
            start = i
            while i < len(expression) and expression[i].isdigit():
                val = val * 10 + int(expression[i])
                i += 1
            nums.append(val)
            print(f"[num] push {val}  | nums={nums}, ops={ops}, token='{expression[start:i]}'")
            i -= 1  # 바깥 while에서 i += 1 할 것이므로 보정
        else:
            # 현재 연산자
            curr_op = ch
            print(f"[op ] read '{curr_op}' | nums={nums}, ops={ops}")

            # 스택 top과 현재 연산자 우선순위 비교 → 기존 연산이 먼저라면 즉시 계산
            while ops and precedence(ops[-1]) >= precedence(curr_op):
                top = ops[-1]
                print(f"      compare top '{top}'({precedence(top)}) >= curr '{curr_op}'({precedence(curr_op)}) → apply")
                b = nums.pop()
                a = nums.pop()
                op = ops.pop()
                res = apply_op(a, b, op)
                nums.append(res)
                print(f"      apply {a} {op} {b} = {res}  | nums={nums}, ops={ops}")

            # 현재 연산자 push
            ops.append(curr_op)
            print(f"[op ] push '{curr_op}' | nums={nums}, ops={ops}")

        i += 1

    # 남은 연산 모두 처리
    print(f"[end] drain ops | nums={nums}, ops={ops}")
    while ops:
        b = nums.pop()
        a = nums.pop()
        op = ops.pop()
        res = apply_op(a, b, op)
        nums.append(res)
        print(f"      apply {a} {op} {b} = {res}  | nums={nums}, ops={ops}")

    return nums[-1]

print(evaluate('1+2*3+2'))  # 9
