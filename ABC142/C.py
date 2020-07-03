ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
a = nl()

sl = sorted(range(len(a)), key=lambda k: a[k])

for s in sl:
    print(s+1)