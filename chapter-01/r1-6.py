def sum_of_squares_of_odds(n: int) -> int:
    return sum([x**2 for x in range(1, n) if x % 2 == 1])


print(sum_of_squares_of_odds(5))
