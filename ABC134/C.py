n = int(input())
a = []

maxa = 0
maxa1 = 0
maxcnt = 0
for i in range(n):
    ai = int(input())
    a.append(ai)
    if maxa < ai:
        maxa1 = maxa
        maxa = ai
        maxcnt = 0
    elif maxa == ai:
        maxcnt += 1
    elif maxa1 < ai:
        maxa1 = ai

for i in range(n):
    if a[i] == maxa:
        if maxcnt > 0:
            print(maxa)
        else:
            print(maxa1)
    else:
        print(maxa)
