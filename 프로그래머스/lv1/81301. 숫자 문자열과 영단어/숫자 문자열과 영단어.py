def solution(s):
    change_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for _str, _num in change_dict.items():
        s = s.replace(_str,_num)
    
    return int(s)