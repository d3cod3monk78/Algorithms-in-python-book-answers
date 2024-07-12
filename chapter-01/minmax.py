from typing import Dict, List


def minmax(*args: int) -> Dict[str, int]:
    num_list: List[int] = list(args)
    length: int = len(num_list)

    for x in range(1, length):
        current: int = num_list[x]
        j: int = x

        while j > 0 and num_list[j - 1] > current:
            num_list[j] = num_list[j - 1]
            j -= 1
        num_list[j] = current

    return {
        'min': num_list[0],
        'max': num_list[len(num_list) - 1]
    }


print(minmax(5, 3, 10, 2, 4, 8))
