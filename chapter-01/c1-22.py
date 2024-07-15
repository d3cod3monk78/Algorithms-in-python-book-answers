def produce_dot_product(array_one: [int], array_two: [int]) -> [int]:
    return [array_one[x] * array_two[x] for x in range(len(array_one))]


data_one = [x for x in range(1, 11)]
data_two = [x for x in range(21, 31)]
print(produce_dot_product(data_one, data_two))
