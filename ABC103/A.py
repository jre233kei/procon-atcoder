ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a = sorted(nl())

print(a[2]-a[0])

