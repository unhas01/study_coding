def solution(lottos, win_nums):
    answer = []
    cnt = 7

    for i in lottos:
        if i == 0: cnt -= 1
        elif i in win_nums: cnt -= 1
    if cnt > 6: answer.append(6)
    else : answer.append(cnt)

    cnt = 7

    for j in lottos:
        if j in win_nums: cnt -= 1
    if cnt > 6: answer.append(6)
    else : answer.append(cnt)

    return answer
    
