def res(s):
    if s == "A+":
        return 4.3
    elif s == "A0":
        return 4.0
    elif s == "A-":
        return 3.7
    elif s == "B+":
        return 3.3
    elif s == "B0":
        return 3.0
    elif s == "B-":
        return 2.7
    elif s == "C+":
        return 2.3
    elif s == "C0":
        return 2.0
    elif s == "C-":
        return 1.7
    elif s == "D+":
        return 1.3
    elif s == "D0":
        return 1.0
    elif s == "D-":
        return 0.7
    elif s == "F":
        return 0.0
    else:
        return ""

print(res(input()))