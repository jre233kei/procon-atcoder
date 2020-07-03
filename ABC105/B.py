ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()

def check(cost):
    if cost == n:
        return 1
    if cost > n:
        return 0

    return check(cost+4) or check(cost+7)

if check(0) == 1:
    print('Yes')
else:
    print('No')