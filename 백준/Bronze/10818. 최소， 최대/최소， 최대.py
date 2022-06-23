input()
numbers = input().split()

_min = _max = int(numbers[0])
for num in numbers[1:]:
    num = int(num)
    if num < _min:
        _min = num
    elif num > _max:
        _max = num
        
print(_min, _max)