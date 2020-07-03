ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

k = ni()

if k%2==1:
    print(k//2*(k//2+1))
else:
    print(k//2*k//2)