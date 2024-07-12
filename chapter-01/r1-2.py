def is_even(n: int) -> bool:
    assert type(n) == int, 'Your input must be an Integer'

    if n > 0:
        while n >= 2:
            n -= 2
    elif n < 0:
        while n <= -2:
            n += 2

    return n == 0


def is_even_bitwise(n: int) -> bool:
    assert type(n) == int, 'Your input must be an Integer'
    return n & 1 == 0


print(is_even(10))
print(is_even(5))
print(is_even(-10))
print(is_even(-3))
