from enum import Flag, auto
from sys import stdin


class DNA(Flag):
    A = auto()
    C = auto()
    G = auto()
    T = auto()
    WILD = A | C | G | T


class Nucleic:
    def __init__(self, *args):
        self.seq = list(args)

    def __iter__(self):
        return iter(self.seq)

    @classmethod
    def create_from_(cls, string):
        return cls(*(cls.char(char) for char in string))

    @staticmethod
    def char(char):
        return {
            "a": DNA.A,
            "c": DNA.C,
            "g": DNA.G,
            "t": DNA.T,
            ".": DNA.WILD,
        }[char]

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self):
        return "".join((i.name if i != DNA.WILD else "*") for i in self.seq)


class SuperNuclic(Nucleic):
    def is_cover(self, other):
        return all(a & b for a, b in zip(self, other))

    def fit_with(self, other):
        for i, val in enumerate(other):
            self.seq[i] &= val
            if not self.seq[i].value:
                raise ValueError


def preprocess_input():
    n, _ = map(int, stdin.readline().split())
    nucleics = []
    for _ in range(n):
        nucleic = Nucleic.create_from_(stdin.readline().rstrip())
        nucleics.append(nucleic)

    return nucleics


def solution():
    nucleics = preprocess_input()
    supers = []
    for nucleic in nucleics:
        for super in supers:
            if super.is_cover(nucleic):
                super.fit_with(nucleic)
                break
        else:
            new = SuperNuclic(*nucleic)
            supers.append(new)

    return len(supers)


answer = solution()
print(answer)
