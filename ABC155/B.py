ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
a = nl()

for ai in a:
  if ai % 2 == 0:
    if ai%3!=0 and ai%5!=0:
      print('DENIED')
      exit()
print("APPROVED")