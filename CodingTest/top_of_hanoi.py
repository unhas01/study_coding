answer = []

def hanoi(num, start, mid, to):
    if num == 1:
        t = []
        t.append(start)
        t.append(to)
        answer.append(t)
        return
    
    hanoi(num-1, start, to, mid)
    
    t = []
    t.append(start)
    t.append(to)
    answer.append(t)
    
    hanoi(num-1,mid, start, to)

def solution(n):
    hanoi(n,1,2,3)
    
    return answer