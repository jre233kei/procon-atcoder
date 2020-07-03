ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))


a, b = nm()

print(max(0,a-2*b))