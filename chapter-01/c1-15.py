import random


def checking_distinct_list(data: [int]) -> bool:
    for x in range(len(data) - 1):
        j: int = x + 1

        while j < len(data):
            if data[x] == data[j]:
                return False
            j += 1
    return True


data_list: [int] = [random.randrange(1, 21) for _ in range(11)]
another_data_list: [int] = [x for x in range(1,11)]
print(data_list)
print(checking_distinct_list(data_list))
print(checking_distinct_list(another_data_list))
