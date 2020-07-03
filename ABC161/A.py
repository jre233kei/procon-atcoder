ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a,b,c = nm()

print("{} {} {}".format(c,a,b))
