from typing import Set
import random


def checking_distinct_list(data: [int]) -> bool:
    for x in range(len(data) - 1):
        j: int = x + 1

        while j < len(data):
            if data[x] == data[j]:
                return False
            j += 1
    return True


def approaching_with_set(data: [int]) -> bool:
    new_set: Set[int] = set()

    for x in data:
        if x in new_set:
            return False
        else:
            new_set.add(x)
    return True


data_list: [int] = [random.randrange(1, 21) for _ in range(11)]
another_data_list: [int] = [x for x in range(1,11)]
print(data_list)
print(checking_distinct_list(data_list))
print(checking_distinct_list(another_data_list))

print()
print(approaching_with_set(data_list))
print(approaching_with_set(another_data_list))
