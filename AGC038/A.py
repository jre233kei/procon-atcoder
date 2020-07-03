import sys

sys.setrecursionlimit(1000 * 1000)

h, w, a, b = map(int, input().split())


def check_mat(m):
    # print()
    # print(m)
    zeros_h = [0] * w

    for i in range(h):
        zeros_w = 0
        for j in range(w):
            if m[i][j] == 0:
                zeros_w += 1
                zeros_h[j] += 1

        if min(zeros_w, w - zeros_w) != a:
            return 0
    # print(zeros_h)
    for i in range(w):
        if min(zeros_h[i], h - zeros_h[i]) != b:
            return 0
    return 1


def check(l, cnt):
    if cnt == h * w:
        mm = []
        for i in range(h):
            mm.append([])
            for j in range(w):
                mm[-1].append(l[i * w + j])
        if check_mat(mm) == 1:
            return mm
        else:
            return None
    mm1 = check(l + [1], cnt + 1)
    if mm1:
        return mm1
    mm2 = check(l + [0], cnt + 1)
    if mm2:
        return mm2


mm = check([], 0)

for i in range(h):
    for j in range(w):
        print(mm[i][j], end='')
    print()

























ans = []

zeros_h2 = [0]*w

for i in range(h):
    zeros_w2 = 0
    ans.append([])
    for j in range(w):
        if zeros_w2 < a and zeros_h2[j] < b:
            ans[i].append(0)
            zeros_w2 += 1
            zeros_h2[j] += 1
        else:
            ans[i].append(1)


for i in range(h):
    for j in range(w):
        print(ans[i][j], end='')
    print()
