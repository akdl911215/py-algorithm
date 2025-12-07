def reverse_string(s: str) -> str:
    if len(s) <= 1:
        return s

    rs = reverse_string(s[1:])
    sz = s[0]

    return rs + sz

print(reverse_string("abcd"))  # "dcba"