def solution(s):
    s = s.lower()
    cnt1 = s.count('p')
    cnt2 = s.count('y')
    if cnt1 == cnt2:
        return True
    else:
        return False
    