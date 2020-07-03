ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
s = [_ for _ in input()]

cnt=0
for i in range(n-2):
  if ''.join(s[i:i+3])=='ABC':
    cnt+=1

print(cnt)