from typing import List


def power_of_two(n: int) -> List[int]:
    return [2 ** x for x in range(n + 1)]


print(power_of_two(10))
