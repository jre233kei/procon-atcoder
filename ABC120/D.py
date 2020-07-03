n, m = map(int, input().split())

cons = []
for i in range(m):
    a, b = map(int, input().split())
    cons.append([a, b])
    cons.append([b, a])
cons = cons[::-1]


def is_connected(a, b, closed):
    if [a, b] in cons:
        return 1
    if [b, a] in cons:
        return 1
    open = []
    for c in cons:
        if c in closed:
            continue
        if c[0] == a or c[1] == a:
            open.append(c)

    for o in open:
        if o[0] == a:
            return is_connected(o[1], b, closed + open)
        if o[1] == a:
            return is_connected(o[0], b, closed + open)

    return 0


def check_connection():
    res = 0
    for i in range(1,n+1):
        for j in range(i+1, n+1):
            ic = is_connected(i, j, [])
            print('{0} {1} {2}'.format(i, j, ic))
            res += ic
    return res


for i in range(m):
    cons.pop()
    cons.pop()
    print(cons)
    print(n * (n - 1) // 2 - check_connection())
