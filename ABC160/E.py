ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

x,y,a,b,c=nm()

ans=0

p=sorted(nl())[::-1][:x]
q=sorted(nl())[::-1][:y]
r=sorted(nl())[::-1]

s=sorted(p+q+r)[::-1]

print(sum(s[:x+y]))



  