def is_valid_parentheses_debug(s: str) -> bool:
    pair = {')': '(', '}': '{', ']': '['}
    stack = []

    for ch in s:
        print(f"문자: {ch}, 현재 스택: {stack}")

        if ch in "({[":
            stack.append(ch)
            print(f"  push -> {stack}")

        elif ch in ")}]":
            if not stack:
                print("  스택이 비어 있는데 닫는 괄호 등장 -> False")
                return False

            top = stack.pop()
            print(f"  pop({top}) -> {stack}")

            if top != pair[ch]:
                print(f"  짝 불일치: {top} != {pair[ch]} -> False")
                return False

    print(f"끝! 최종 스택: {stack}")
    return len(stack) == 0


print(is_valid_parentheses_debug("({[]})"))
