ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))


n = ni()

s = [_ for _ in input()]

ans = []

last = ""
for i in range(n):
    if s[i] == last:
        continue
    ans += s[i]
    last = s[i]

print(len(ans))
