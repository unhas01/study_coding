def solution(files):
    answer = []

    for f in files:
        head, number, tail = '', '', ''
        for i in range(len(f)):
            if f[i].isdigit():
                head = f[:i]
                number = f[i:]

                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break

                answer.append([head,number,tail])
                break

    answer.sort(key = lambda x:(x[0].lower(), int(x[1])))


    return [''.join(i) for i in answer]

f1 = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
f2 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]

print(solution(f1))
print(solution(f2))