from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for i in course:
        temp = []
        for o in orders:
            o = sorted(o)
            temp.extend(combinations(o, i))

        count = Counter(temp)

        if count:
            if max(count.values()) >= 2:
                for key, value in count.items():
                    if value == max(count.values()):
                        answer.append("".join(key))

    return sorted(answer)


o1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
c1 = [2,3,4]
o2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
c2 = [2,3,5]

print(solution(o1,c1))
print(solution(o2,c2))