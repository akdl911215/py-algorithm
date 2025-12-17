def is_palindrome(s: str) -> bool:
    # 기저 사례
    if len(s) <= 1:
        return True

    zero = s[0]
    one = s[-1]
    if zero != one:
        return False

    result = is_palindrome(s[1:-1])
    return result

# 테스트
print(is_palindrome("level"))  # True
print(is_palindrome("abba"))   # True
print(is_palindrome("hello"))  # False