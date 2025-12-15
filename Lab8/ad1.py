import re


def is_float(value: str) -> bool:
    pattern = r"^-?\d+\.\d+$"
    return bool(re.match(pattern, value))


print(is_float("123.45"))
print(is_float("12345"))
print(is_float("abc"))
print(is_float("123,45"))
