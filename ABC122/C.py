n, q = map(int, input().split())
s = input()

ss = [0] * (n+1)

for i in range(n - 1):
    if s[i] == 'A' and s[i + 1] == 'C':
        ss[i+1] = 1

sss = [0] * (n+1)
cnt = 0
for i in range(n+1):
    cnt += ss[i]
    sss[i] = cnt


for i in range(q):
    l, r = map(int, input().split())
    print(sss[r-1] - sss[l-1])

