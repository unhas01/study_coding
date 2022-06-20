def solution(numbers, hand):
    answer = ''

    Pleft = 10    # '*'
    Pright = 12   # '#'

    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:         # 1,4,7은 왼손으로
            answer += 'L'
            Pleft = numbers[i]
        elif numbers[i] in [3, 6, 9]:       # 3,6,9는 오른손으로
            answer += 'R'
            Pright = numbers[i]
        else:                               # 2,5,8,0은 거리 계산 + hand 사용
            # 거리계산
            numbers[i] = 11 if numbers[i] == 0 else numbers[i]

            L = abs(numbers[i] - Pleft)
            R = abs(numbers[i] - Pright)

            if sum(divmod(L, 3)) > sum(divmod(R, 3)):
                answer += 'R'
                Pright = numbers[i]
            elif sum(divmod(L, 3)) < sum(divmod(R, 3)):
                answer += 'L'
                Pleft = numbers[i]
            else:   # 거리가 같은 경우
                if hand == 'right':
                    answer += 'R'
                    Pright = numbers[i]
                else:
                    answer += 'L'
                    Pleft = numbers[i]

    return answer

n = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
h = "right"
print(solution(n, h))