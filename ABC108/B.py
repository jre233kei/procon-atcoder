ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

x1, y1, x2, y2 = nm()

lx = x2-x1
ly = y2-y1

print(x2-ly)
print(y2+lx)
print(x1-ly)
print(y1+lx)