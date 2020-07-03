n, m = map(int, input().split())

stairs = [0] * (n+1)
broken_stairs = [0] * (n+1)

stairs[0] = 1

for i in range(m):
    broken_stairs[int(input())] = 1

for i in range(n):
    if broken_stairs[i+1] == 0:
        stairs[i+1] += stairs[i]
    if i >= n-1:
        break
    if broken_stairs[i+2] == 0:
        stairs[i+2] += stairs[i]

print(stairs[n] % (10**9+7))