ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n=ni()


cnt=[0]*(n+1)

for x in range(1,n+1):
  if x**2+x>n:
    break
  for y in range(x,n+1):
    if x**2+y**2+x*y+x+y>n:
      break
    for z in range(y,n+1):
      num = x**2+y**2+z**2+x*y+y*z+x*z
      if num > n:
        break
      if x==y==z:
        cnt[num]+=1
      elif x==y:
        cnt[num]+=3
      elif y==z:
        cnt[num]+=3
      elif x==z:
        cnt[num]+=3
      else:
        cnt[num]+=6

for i in range(1,n+1):
  print(cnt[i])
