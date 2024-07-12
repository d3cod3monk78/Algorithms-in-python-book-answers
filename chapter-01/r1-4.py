def sum_of_squares(n: int) -> int:
    return sum([x**2 for x in range(1, n)])


print(sum_of_squares(5))
