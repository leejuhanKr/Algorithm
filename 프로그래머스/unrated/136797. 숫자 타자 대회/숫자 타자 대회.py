def solution(numbers):
    MAX = 1000000
    defaultMAX = [MAX] * 10
    dist = [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
            [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
            [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
            [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
            [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
            [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
            [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
            [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
            [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
            [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]

    prev = dict(zip(range(10), defaultMAX))
    prev[6] = 0
    prevNum = 4

    for number in numbers:
        number = int(number)
        if number == prevNum:
            for i in range(10):
                prev[i] += 1
            continue
        new = dict(zip(range(10), defaultMAX))
        for i in range(10):
            if i != prevNum:
                new[i] = prev[i] + dist[number][prevNum]
                new[prevNum] = min(new[prevNum], prev[i]+dist[number][i])
        prev = new
        prevNum = number

    return min(prev.values())

            