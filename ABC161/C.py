ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,k = nm()

print(min(n%k,abs(k-n%k)))