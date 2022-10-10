import re


def solution(new_id):
    res = new_id
    res = res.lower()  # 1
    res = re.sub("[^\w\-_.]", "", res)  # 2
    res = re.sub("\.+", ".", res)  # 3
    res = re.sub("^\.|\.$", "", res)  # 4
    res = re.sub("^$", "a", res)  # 5
    res = re.sub("\.$", "", res[:15])  # 6
    res = res.ljust(3, res[-1])  # 7
    return res