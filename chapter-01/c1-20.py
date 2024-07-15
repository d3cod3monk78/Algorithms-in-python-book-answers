from typing import Set
import random


# Bruteforce solution
def custom_shuffle_bruteforce(data: [int]) -> [int]:
    array: [int] = [None] * len(data)
    choices: Set[int] = set()

    for x in range(len(data)):
        added: bool = False

        while added == False:
            custom_choice = random.randint(0, len(data) - 1)
            if custom_choice not in choices:
                array[custom_choice] = data[x]
                choices.add(custom_choice)
                added = True

    return array


data_list: [int] = [x for x in range(1, 11)]
print(custom_shuffle_bruteforce(data_list))
print()


# Gradual swap method
def custom_shuffle_gradual(data: [int]) -> [int]:
    length: int = len(data)

    for x in range(length):
        index = random.randint(0, length - 1 - x)
        data[index], data[length - 1 - x] = data[length - 1 - x], data[index]

    return data


data_list: [int] = [x for x in range(1, 11)]
print(custom_shuffle_gradual(data_list))
