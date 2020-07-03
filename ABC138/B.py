n = int(input())
ans = 0.0
nn = [int(ni) for ni in input().split()]
for i in range(n):
    ans += (1/float(nn[i]))

print(1/ans)