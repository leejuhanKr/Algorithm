def solution(num_list, n):
    return [*zip(*(num_list[i::n] for i in range(n)))]