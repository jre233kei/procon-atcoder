ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
b = nl()


def insert(bl, l, lo):

    if l is None:
        return
    if len(l) == n:
        if l == b:
            return 1, lo
        return
    for i in range(len(bl)):

        if len(l) < bl[i]-1:
            return
        ll = [li for li in l]
        ll.insert(bl[i] - 1, bl[i])
        res = insert(bl[0:i] + bl[i+1:n], ll, lo+[bl[i]])
        if res is not None:
            return res


ans = insert(b, [], [])
if ans:
    print(' '.join([str(s) for s in ans[1]]))
else:
    print(-1)
