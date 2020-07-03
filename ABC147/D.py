ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
a = nl()

num = 1000000007

ans = 0

for i in range(n):
  for j in range(i,n):
    ans += (a[i] ^ a[j]) % num

print(ans % num)