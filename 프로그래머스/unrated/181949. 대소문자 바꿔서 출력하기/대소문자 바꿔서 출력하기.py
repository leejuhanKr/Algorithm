str = input()
arr = list(str)
def change(val):
    if val.islower():
        return val.upper()
    return val.lower()
print(''.join(map(change,arr)))