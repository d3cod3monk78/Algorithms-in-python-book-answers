def equivalent_positive_index(string: str, k: int) -> int:
    length_of_str: int = len(string)
    assert 0 > k >= -length_of_str, 'Your input is on the range of length of string'
    return length_of_str + k


print(equivalent_positive_index('bitches', -5))
