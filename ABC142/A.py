ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()

if n%2 == 1:
    print(((n+1)/2)/n)
else:
    print(n/2/n)