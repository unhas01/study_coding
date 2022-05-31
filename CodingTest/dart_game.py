def solution(dartResult):
    li = []
    dartResult = dartResult.replace('10', 'A')

    for i in dartResult:
        if i.isdigit() or i == 'A':
            li.append(10 if i == 'A' else int(i))
        elif i in ('S', 'D', 'T'):
            number = li.pop()
            if i == 'S':
                li.append(number ** 1)
            elif i == 'D':
                li.append(number ** 2)
            elif i == 'T':
                li.append(number ** 3)
        elif i == '#':
            li[-1] *= -1
        elif i == '*':
            number = li.pop()
            if len(li):
                li[-1] *= 2
            li.append(2 * number)

    return sum(li)