def is_valid_parentheses(s: str) -> bool:
    pair = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []

    for ch in s:
        if ch in '({[':
            stack.append(ch)

        elif ch in ')]}':
            if not stack:
                return False

            top = stack.pop()
            if top != pair[ch]:
                return False

        else:
            pass

    return len(stack) == 0


# print(is_valid_parentheses("({[]})"))  # True
print(is_valid_parentheses("([)]"))    # False
print(is_valid_parentheses("(()"))     # False
print(is_valid_parentheses(")("))     # False