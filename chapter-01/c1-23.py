def write_on_index(array: [int], index: int, value: int = 100):
    try:
        array[index] = value
    except IndexError:
        print("Don't try buffer overflow attack in python")


array: [int] = [x for x in range(1, 6)]
write_on_index(array, 3, 10)
write_on_index(array, 1, 21)
write_on_index(array, 10, 98)
