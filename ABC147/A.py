ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))


a = nl()

if(sum(a)>=22):
  print("bust")
else:
  print("win")