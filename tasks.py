from typing import List
from functools import reduce
from operator import mul


def replace_quotes(string: str) -> str:
    return string.translate(string.maketrans({"'": '"', '"': "'"}))


def is_palindrome(string: str):
    unused_chars = (',', '.', '-', '—', '!', '?', ':', ';', '\'', '"', ' ')

    for char in unused_chars:
        string = string.replace(char, "")

    string = string.lower()
    return string[::1] == string[::-1]


def split_str(string: str, separator: str, maxsplit: int = -1):
    strings = []
    sep_start = 0
    sep_old_start = 0

    sep_start = string.find(separator)

    if sep_start == -1:
        strings.append(string)
        return strings

    strings.append(string[0:sep_start])

    while True:
        sep_old_start = sep_start
        sep_start = string.find(separator, sep_start + len(separator))

        if sep_start == -1:
            strings.append(string[sep_old_start + len(separator):])
            return strings

        if len(strings) == maxsplit + 1:
            strings[maxsplit] += string[sep_old_start:]
            return strings

        strings.append(string[sep_old_start + len(separator):sep_start])


def split_by_index(string: str, indexes: List[int]):
    strings = []
    indexes.insert(0, 0)
    pre_i = 0
    for i in indexes[1:]:
        strings.append(string[pre_i:i])
        pre_i = i
    if len(string) > indexes[-1]:
        strings.append(string[indexes[-1]:])
    return strings


def get_digits(array: int):
    return tuple(str(array)[::1])


def get_longest_word(string: str):
    if not string:
        raise Exception('Empty string!')
    return max(string.split(), key=len)


def product_array(values: List[int]):
    res = reduce(mul, values)
    return [res // v for v in values]


def get_pairs(values: list):
    if len(values) == 1:
        return

    new_list = []

    for i, j in zip(values[:-1], values[1:]):
        new_list.append((i, j))
    return new_list


inp = input()
while inp != 'q':
    # print(replace_quotes(inp))
    # print(is_palindrome(inp))
    # print(inp.split('.1.', 2))
    # print(split_str(inp, '.1.', 2))
    # print(get_longest_word(inp))
    # print(get_digits(int(inp)))
    # print(split_by_index(inp, [6, 8, 12, 13, 18]))
    # print(product_array([1, 2, 3, 4, 5]))
    # print(get_pairs([1, 2]))
    # a = 12345 is 12345
    # print(a)
    inp = input()
