ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))


ans=9999
diff=9999

x,n=nm()
p=set(nl())

for i in range(102):
  if i not in p:
    if abs(x-i)==diff:
      if i<ans:
        ans=i
    elif abs(x-i)<diff:
      diff = abs(x-i)
      ans = i

print(ans)

