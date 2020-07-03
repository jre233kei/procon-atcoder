ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
b = nl()

ans = []

for i in range(n):
    for j in range(len(b))[::-1]:
        if b[j] == j + 1:
            ans.append(b[j])
            del b[j]
            break
        if j == 0:
            print(-1)
            exit()

print(' '.join([str(_) for _ in reversed(ans)]))
