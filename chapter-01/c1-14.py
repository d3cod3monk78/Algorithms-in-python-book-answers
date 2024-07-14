from typing import List, Set


def checking_couples(data: [int]) -> List[Set[int]]:
    result_list: List[Set[int, int]] = []

    for x in range(len(data) - 1):
        j: int = x + 1
        while j < len(data):
            if (not data[x] == data[j]) and (not data[x] * data[j] % 2 == 0):
                result_list.append({data[x], data[j]})
            j += 1
    return result_list


data_list: [int] = [x for x in range(1, 11)]
print(checking_couples(data_list))
