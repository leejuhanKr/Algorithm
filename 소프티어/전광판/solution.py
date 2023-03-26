from sys import stdin
from operator import xor

digit_ = {
    "0": 0b1110111,
    "1": 0b0010010,
    "2": 0b1011101,
    "3": 0b1011011,
    "4": 0b0111010,
    "5": 0b1101011,
    "6": 0b1101111,
    "7": 0b1110010,
    "8": 0b1111111,
    "9": 0b1111011,
    "_": 0,
}


def preprocess_input():
    T = int(stdin.readline())
    return (stdin.readline().split() for _ in range(T))


def xor_digit(a, b) -> int:
    diff = f"{xor(digit_[a], digit_[b]):b}"
    return sum(int(i) for i in diff)


def get_change_between(str_num_1, str_num2) -> int:
    max_len = max(len(v) for v in (str_num_1, str_num2))
    str_num_1, str_num2 = f"{str_num_1:_>{max_len}}", f"{str_num2:_>{max_len}}"
    return sum(xor_digit(a, b) for a, b in zip(str_num_1, str_num2))


def solution():
    change = 0
    for prev, tmp in preprocess_input():
        change = get_change_between(prev, tmp)
        print(change)


solution()
