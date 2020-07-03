n = int(input())
ans = 0
for i in range(n):
    inp = input().split()
    x = float(inp[0])
    u = inp[1]
    if u == 'JPY':
        ans += x
    if u == 'BTC':
        ans += x*380000

print(ans)