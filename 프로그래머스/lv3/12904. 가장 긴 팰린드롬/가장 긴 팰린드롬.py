def in_range(n, l):
  # IndexError Check
    return n < l and n >= 0

def solution(s):
    answer = 0
    n = len(s)
    
    for i in range(n):
        # 짝수 길이 팰린드롬
        start, end = i, i + 1
        l = 0
        while True:
            if in_range(start, n) and in_range(end, n):
                if s[start] == s[end]:
                    l += 2
                    start -= 1
                    end += 1
                else:
                    answer = max(answer, l)
                    break
            else:
                answer = max(answer, l)
                break
        # 홀수 길이 팰린드롬
        start, end = i - 1, i + 1
        l = 1
        while True:
            if in_range(start, n) and in_range(end, n):
                if s[start] == s[end]:
                    l += 2
                    start -= 1
                    end += 1
                else:
                    answer = max(answer, l)
                    break
            else:
                answer = max(answer, l)
                break
                
    return answer