from typing import Tuple


def count_all_vowels(string: str) -> int:
    vowel_count: int = 0

    for x in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += string.count(x)

    return vowel_count


def count_vowel_by_vowel(string: str) -> [Tuple[str, int]]:
    array: [Tuple[str, int]] = []

    for x in ['a', 'e', 'i', 'o', 'u']:
        array.append((x, string.count(x)))

    return array


print(count_all_vowels('what the hell is going on with you'))
print(count_vowel_by_vowel('what the hell is going on with you'))
