INF = (10 ** 13)

x, y, z, k = map(int, input().split())

a = sorted(list(map(int, input().split())))[::-1]
b = sorted(list(map(int, input().split())))[::-1]
c = sorted(list(map(int, input().split())))[::-1]

ai = 0
bi = 0
ci = 0

print(a[ai] + b[bi] + c[ci])

ks = set()
for i in range(k):
    a0 = a[ai]
    b0 = b[bi]
    c0 = c[ci]
    if ai < x - 1:
        a1 = a[ai + 1]
    else:
        a1 = -INF
    if bi < x - 1:
        b1 = b[bi + 1]
    else:
        b1 = -INF
    if ci < x - 1:
        c1 = c[ci + 1]
    else:
        c1 = -INF

    if str([ai + 1, bi, ci]) in ks:
        a_sub = -INF
    else:
        a_sub = a1 + b0 + c0
    if str([ai, bi + 1, ci]) in ks:
        b_sub = -INF
    else:
        b_sub = a0 + b1 + c0
    if str([ai, bi, ci + 1]) in ks:
        c_sub = -INF
    else:
        c_sub = a0 + b0 + c1

    print('---')
    print(a_sub)
    print(b_sub)
    print(c_sub)

    if max(a_sub, b_sub, c_sub) == a_sub:
        ai += 1
        print(a[ai] + b[bi] + c[ci])
        ks.add(str([ai, bi, ci]))
        continue
    if max(a_sub, b_sub, c_sub) == b_sub:
        bi += 1
        print(a[ai] + b[bi] + c[ci])
        ks.add(str([ai, bi, ci]))
        continue
    if max(a_sub, b_sub, c_sub) == c_sub:
        ci += 1
        print(a[ai] + b[bi] + c[ci])
        ks.add(str([ai, bi, ci]))
        continue
