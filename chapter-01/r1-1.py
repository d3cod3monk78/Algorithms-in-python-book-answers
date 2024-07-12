def is_multiply(n: int, m: int) -> bool:
    if m == 1:
        return False
    return n % m == 0


print(is_multiply(10, 5))
print(is_multiply(10, 3))
