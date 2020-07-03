n = int(input())

ans = 0
max_ = 0
for i in range(n):
    num = int(input())
    ans += num
    max_ = max(max_, num)

print(ans - max_//2)