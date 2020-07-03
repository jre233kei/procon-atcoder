import sys

sys.setrecursionlimit(1000 * 1000)

h, w, a, b = map(int, input().split())
ans = []

zeros_h2 = [0]*w

for i in range(h):
    zeros_w2 = 0
    ans.append([])
    for j in range(w):
        nx = 1
        if zeros_w2 < a and zeros_h2[j] < b:
            nx = 0

        if nx == 0:
            ans[i].append(0)
            zeros_w2 += 1
            zeros_h2[j] += 1
        else:
            ans[i].append(1)


for i in range(h):
    for j in range(w):
        print(ans[i][j], end='')
    print()
