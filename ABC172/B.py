ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

s = [_ for _ in input()]
t = [_ for _ in input()]
cnt=0
for i in range(len(s)):
  if s[i]!=t[i]:
    cnt+=1
print(cnt)