from collections import deque

T = int(input())    # 테스트 케이스 크기

for i in range(T):
    p = list(input())   # 수행할 함수 p
    n = int(input())    # 배열의 크기
    li = input()        # 배열형태 정수
    d = deque(li[1: -1].split(',') )
    
    chk = 0
    re_cnt = 0
    
    if n == 0:
        d = []

    for j in p:
        if j == 'R':            # 'R' 마다 reverse()하면 시간 초과
            re_cnt += 1         # 짝수 == reverse하지 않은 것과 동일
        else:
            if len(d) < 1:
                print('error')
                chk = 1
                break
            else:
                if re_cnt % 2 == 0:
                    d.popleft()
                else:
                    d.pop()

    if chk == 0:
        if re_cnt % 2 == 0:
            print('[' + ",".join(d) + "]")
        else:
            d.reverse()
            print('[' + ",".join(d) + "]")
