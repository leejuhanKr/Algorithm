def solution(distance, scope, times):
    answer = [distance]

    for sc_index, sc in enumerate(scope):
        a = sum(times[sc_index])
        b = times[sc_index][0]
        for s in range(min(sc), max(sc)+1):
            if 0 < s % a <= b:
                answer.append(s)

    return min(answer)