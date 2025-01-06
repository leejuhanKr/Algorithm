def product(arr: list, repeat: int):
    if repeat == 0:
        yield tuple()
        return
    for el in arr:
        for rest in product(arr, repeat - 1):
            yield (el,) + rest
    

def sol(n: int, k: int, arr: list[int]):
    arr.sort(reverse=True)
    digit = len(str(n))
    
    while True:
        for d in range(digit, 0, -1):
            for p in product(arr, repeat=d):
                v = int("".join(map(str, p)))
                if v <= n:
                    return v
    
def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    res = sol(n, k, arr)
    print(res)


if __name__ == "__main__":
    main()