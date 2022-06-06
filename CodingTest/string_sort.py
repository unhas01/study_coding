def solution(strings, n):
    answer = sorted(sorted(strings), key=lambda x: x[n])
    return answer



st = ["abce", "abcd", "cdx"]
print(solution(st, 2))