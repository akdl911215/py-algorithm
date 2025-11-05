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
        if expression[i] == ' ':
            i += 1
            continue

        expression_isdigit = expression[i].isdigit()
        print('expression_isdigit : ', expression_isdigit)
        if expression_isdigit:
            val = 0

            while i < len(expression) and expression[i].isdigit():
                val = val * 10 + int(expression[i])
                i += 1
            nums.append(val)
            i -= 1
        else:
            while ops and precedence(ops[-1]) >= precedence(expression[i]):
                b = nums.pop()
                a = nums.pop()
                op = ops.pop()
                nums.append(apply_op(a, b, op))
            ops.append(expression[i])
        i += 1

    while ops:
        b = nums.pop()
        a = nums.pop()
        op = ops.pop()
        nums.append(apply_op(a, b, op))
    return nums[-1]

print(evaluate('1+2*3+2')) # 9
