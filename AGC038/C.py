h, w, a, b = map(int, input().split())

ans = []

for i in range(h):
    ans.append([])
    for j in range(w):
        if i < b and j < a:
            ans[i].append(0)
        elif i >= b and j >= a:
            ans[i].append(0)
        else:
            ans[i].append(1)

for i in range(h):
    for j in range(w):
        print(ans[i][j], end='')
    print()
