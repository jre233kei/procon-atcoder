import sys
import bisect

sys.setrecursionlimit(10 ** 8)

n, k = map(int, input().split())
d = list(map(int, input().split()))


def put_queue(dd, l, v):
    if l == k:
        return 0

    if len(dd) > 0:
        a = dd[0] + put_queue(dd[1:], l + 1, bisect.insort(v, [dd[0]]))
        b = dd[-1] + put_queue(dd[:-1], l + 1, bisect.insort(v, [dd[-1]]))
    else:
        a = 0
        b = 0
    if len(v) > 0:
        minv = v[0]
        c = -minv + put_queue([minv] + dd, l + 1, v[1:])
        d = -minv + put_queue(dd + [minv], l + 1, v[1:])
        return max(a, b, c, d)
    return max(a, b)


print(max(0, put_queue(d, 0, [])))
