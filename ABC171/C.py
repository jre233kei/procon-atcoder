ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()-1

ans=[]
while n>=0:
  ans.append(chr(ord('a')+n%26))
  n//=26
  n-=1
print(''.join(ans[::-1]))