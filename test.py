# # class DB:
# #     def __init__(self):
# #         self.db = [[]]

# #     def set_size(self, x_size, y_size):
# #         self.db = [[Record(None) for _ in range(y_size)] for _ in range(x_size)]

# #     def __getitem__(self, pos):
# #         record = self.db[pos.x][pos.y]
# #         if not isinstance(record.value, Ref):
# #             return record.value
# #         self.__getitem__(record.value.ref)

# #     def __setitem__(self, pos, value):
# #         self[pos] = Record(value)

# #     def update(self, pos, value):
# #         self[pos] = Record(value)

# #     def replace_all(self, value1, value2):
# #         Record(value1).value = value2

# #     def merge(self, pos1, pos2):
# #         if self[pos1]:
# #             self.update(pos2, Ref(pos1))
# #             return
# #         if self[pos2]:
# #             self.update(pos1, Ref(pos2))
# #             return

# #     def __str__(self):
# #         _str = []
# #         for r in range(len(self.db)):
# #             _row = [str(self[Pos(r, c)]) for c in range(len(self.db[0]))]
# #             _str.append(", ".join(_row))
# #         return "\n".join(_str)


# class Record:
#     def __init__(self, val):
#         self.val = val

#     def __str__(self):
#         return str(self.val)


# class CacheAble(Record):  # cacheable record
#     cache = {}

#     def __new__(cls, value):
#         key = hash(value)
#         if key not in cls.cache:
#             cls.cache[key] = object.__new__(cls)
#         return cls.cache[key]


# class Ref(Record):
#     pass


# class Null(Record):
#     created = None

#     def __new__(cls):
#         if not cls.created:
#             cls.created = object.__new__(cls)
#         return cls.created

#     def __init__(self):
#         self.val = None

#     def __str__(self):
#         return "Empty"


# # class Pos:
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y


# # class IdGenerator:
# #     id = -1

# #     def __call__(self):
# #         IdGenerator.id += 1
# #         return IdGenerator.id


# # def solution(commands):
# #     id_gen = IdGenerator()
# #     db = DB()
# #     db.set_size(3, 4)
# #     db.update(Pos(1, 1), "1")
# #     # db.update(Pos(1, 2), "1")
# #     # db.update(Pos(1, 2), "2")
# #     # db.replace_all("1", "3")
# #     # db.merge(Pos(1, 1), Pos(0, 0))
# #     # print(db.update(Pos(0, 0), Ref(Pos(2, 2))))
# #     # print(db[Pos(0, 0)])
# #     # print(isinstance(db[Pos(0, 0)], Ref))
# #     # print(db[Pos(1, 1)])
# #     # print(isinstance(db.db[0][0].value, Ref))

# #     # print(db.db[0][0].value)
# #     # print(isinstance(db.db[0][0].value, Ref))
# #     # print(Ref(1))
# #     # print(isinstance(Ref(1), Ref))


# # solution(None)

# # class Record:
# #     def __init__(self, value):
# #         self.val = value


# class DataTable:
#     def __init__(self):
#         self.col_size = 0
#         self.row_size = 0
#         self.table = []

#     @classmethod
#     def instance(cls, row_size, col_size):
#         table = cls()
#         table.col_size = col_size
#         table.row_size = row_size
#         table.table = [[Null()] * col_size for _ in range(row_size)]
#         return table

#     # def __getitem__(self, pos):
#     #     r_idx, c_idx = pos
#     #     return self.table[r_idx][c_idx]

#     # def __setitem__(self, pos, val):
#     #     r_idx, c_idx = pos
#     #     self.table[r_idx][c_idx] = val

#     def __str__(self):
#         _str = ""
#         for r_idx, row in enumerate(self.table):
#             _row_str = f"{r_idx}| {' '.join(f'{str(datum): ^5}' for datum in row)}\n"
#             _str += _row_str
#         return _str

#     def _get(self, r_idx, c_idx):
#         return self.table[r_idx][c_idx]

#     def get(self, r_idx, c_idx):
#         record = self._get(r_idx, c_idx)
#         if (record is Ref):
#             return record.val
#         return record

#     def _set(self, r_idx, c_idx, record):
#         self.table[r_idx][c_idx] = record

#     def _refer(self, pos1, pos2):
#         if pos1 == pos2:
#             return
#         record1, record2 = self.get(*pos1), self.get(*pos2)
#         if record1 is not Null:
#             r_idx, c_idx = pos1
#             self._set(r_idx, c_idx, Ref(pos2))
#             return
#         if record2 is not Null:
#             r_idx, c_idx = pos2
#             self._set(r_idx, c_idx, Ref(pos1))
#             return

#     def _unrefer(self, pos1, pos2):


#     def update(self, r_idx, c_idx, val):
#         self.table[r_idx][c_idx] = CacheAble(val)


# table = DataTable.instance(5, 5)
# print(table)

# a = nos
# b = nnoooss
# a=pps
# b=pppppsssss

# nos 111
# nnooss 222
# nnoooss 232

# pps 21
# ppppss 42
# ppppssss 44
# pppppsssss 55
# pppppsssss 55
# pppppss 53
# ppps 31
# pps 21
# ppp pppppp
# 1이면 복사하면 안됨
# 2이면 -=1
# 3이면 -=1 또느 -=2
# 6이면

a, b, c = 1, 1, 1
s = [a, b, c]


# def foo(args, copied=3):
#     # diff = [3,0,0]
#     # while diff==[0,0,0]:
#     if not args or copied < 1:
#         yield args
#         return
#     front, *rest = args

#     # if front >= 3 and copied >= 3:
#     #     yield from ([front + 3, *res] for res in foo(rest, copied=copied - 3))
#     # if front >= 2 and copied >= 2:
#     #     yield from ([front + 2, *res] for res in foo(rest, copied=copied - 2))
#     # if front >= 1 and copied >= 1:
#     #     yield from ([front + 1, *res] for res in foo(rest, copied=copied - 1))
#     # if front >= 0 and copied >= 0:
#     #     yield from ([front + 0, *res] for res in foo(rest, copied=copied - 0))
#     for diff in range(3, 0, -1):
#         if front >= diff and copied >= diff:
#             # yield from ([front + diff, *res] for res in foo(rest, copied=copied - diff))
#             for res in foo(rest, copied=copied - diff):
#                 if res and (not res[0]):
#                     continue
#                 yield [front + diff, *res]
#     yield from ([front, *res] for res in foo(rest, copied=copied))


# for i in foo([3, 3, 3], copied=3):
#     print(i)
# # front, *rest = [1, 2, 3]
# # print(front, rest)
# a = [*foo([3, 3, 3], copied=3)]
# print(len(a))

a = [3, 3, 3]

# flag // 2:> 둘다 1: 무조건 뒤에 증가 0: 뒤에는 증가하지 않음
def foo(args, copied=3, started=False, ended=False):
    # print(args)
    if not args:
        return
    if copied <= 0 and ended:
        yield args
        return
    head, *rest = args

    for diff in range(min(head, copied), 0, -1):
        for _ended in (False, True):
            for _rest in foo(rest, copied=copied - diff, started=True, ended=_ended):
                yield [head + diff, *_rest]
    if not started:
        for _rest in foo(rest, copied=copied, started=True, ended=False):
            yield [head, *_rest]


for x in foo(a, 3, False, False):
    print(x)
