ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

s = [_ for _ in input()]
t = [_ for _ in input()]

for i in range(len(s)):
  s = [s[-1]] + s[:-1]
  if s==t:
    print('Yes')
    exit()
print('No')