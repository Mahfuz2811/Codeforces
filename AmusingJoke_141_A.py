def amusingJoke(st1, st2, st3):
    check1 = [0]*100
    check2 = [0]*100

    for ch in st1+st2:
        check1[ord(ch)] += 1

    for ch in st3:
        check2[ord(ch)] += 1

    if len(st1+st2) != len(st3):
        return "NO"

    for ch in st3:
        if check1[ord(ch)] != check2[ord(ch)]:
            return "NO"

    return "YES"


s1 = input()
s2 = input()
s3 = input()

print(amusingJoke(s1, s2, s3))
