from typing import List
import time


def reverse_array(data: [int]) -> List[int]:
    return data[::-1]


def another_way(data: [int]) -> List[int]:
    data.reverse()
    return data


data_list: [int] = [x for x in range(1, 10)]
start_time_of_reverse_array = time.time_ns()
print(reverse_array(data_list))
end_time_of_reverse_array = time.time_ns()
print(f'Elapsed time for reverse_array function: {end_time_of_reverse_array - start_time_of_reverse_array}ns')

start_time_of_another_way = time.time_ns()
print(another_way(data_list))
end_time_of_another_ray = time.time_ns()
print(f'Elapsed time for reverse_array function: {end_time_of_another_ray - start_time_of_another_way}ns')
