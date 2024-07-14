import random


def rand_choice(data: [int]) -> int:
    return data[random.randrange(0, len(data))]


data: [int] = [x for x in range(1, random.randint(10, 100))]

for _ in range(random.randint(100, 200)):
    print(rand_choice(data), end=' ')
