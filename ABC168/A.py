ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()

nn = n%10

if nn == 3:
  print('bon')
elif nn == 0 or nn== 1 or nn==6 or nn==8:
  print('pon')
else:
  print('hon')
