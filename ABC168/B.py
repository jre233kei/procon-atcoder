ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

k = ni()
s = input()

if len(s) > k:
  print(s[:k]+'...')
else:
  print(s)