def solution(N, stages):
    answer = []
    all = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)
        if all == 0:
            fail = 0
        else:
            fail = count / all

        all -= count
        answer.append((i, fail))

    answer = sorted(answer, key = lambda x : x[1],reverse = True)
    answer = [i[0] for i in answer]
    return answer