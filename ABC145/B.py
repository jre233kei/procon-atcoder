ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
s = input()

if s[:n//2] == s[n//2:]:
  print('Yes')
else:
  print('No')