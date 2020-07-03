n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

temp_diff = 10**10
ans = 0

for i in range(n):
    temp = abs(a-(t-h[i]*0.006))
    if temp < temp_diff:
        temp_diff = temp
        ans = i+1

print(ans)