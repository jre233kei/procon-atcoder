ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()

w = []
seen = []
for i in range(n):
    w.append(input())

for i in range(n-1):
    if w[i] in seen or w[i+1] in seen:
        print('No')
        exit()
    if w[i][-1] != w[i+1][0]:
        print('No')
        exit()
    seen.append(w[i])

print('Yes')
