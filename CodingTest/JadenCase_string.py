def solution(s):
    s = s.split(" ")

    for i in range(len(s)):
        s[i] = s[i][:1].upper() + s[i][1:].lower()
        
    return ' '.join(s)

print(solution("3people unFollowed me"))
print(solution("for the last week"))