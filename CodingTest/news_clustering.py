from math import floor

def solution(str1, str2):
    answer = 0
    
    a = []
    b = []
    for i in range(len(str1) - 1):
        t = str1[i:i+2].lower()
        if t.isalpha() or len(t) < 2:
            a.append(t)
        else:
            continue
    
    for i in range(len(str2) - 1):
        t = str2[i:i+2].lower()
        if t.isalpha() or len(t) < 2:
            b.append(t)
        else:
            continue
    
    # 교집합 
    same = set(a) & set(b)

    # 합집합
    all = set(a) | set(b)

    if len(all) == 0:
        return 65536

    smae_len = sum([min(a.count(i), b.count(i)) for i in same])
    all_len = sum([max(a.count(i), b.count(i)) for i in all])

    answer = floor((smae_len / all_len) * 65536)

    return int(answer)

s1 = 'FRANCE'
s2 = 'french'
s3 = 'handshake'
s4 = 'shake hands'
s5 = 'E=M*C^2'
s6 = 'e=m*c^2'
s7 = 'aa1+aa2'
s8 = 'AAAA12'

print(solution(s1,s2))
print(solution(s3,s4))
print(solution(s5,s6))
print(solution(s7,s8))