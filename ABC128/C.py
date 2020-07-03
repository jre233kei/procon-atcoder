n, m = map(int, input().split())

s = []
k = []
for i in range(m):
    ks = list(map(int, input().split()))
    k.append(ks[0])
    s.append(ks[1:])

p = list(map(int, input().split()))


def check_switch(ss):
    for i in range(m):
        sum_switch = 0
        for j in range(k[i]):
            sum_switch += ss[s[i][j] - 1]
        if sum_switch % 2 != p[i]:
            return 0
    return 1


def check(switches, l):
    if l == n:
        return check_switch(switches)
    return check(switches+[0], l + 1) + check(switches+[1], l + 1)


print(check([], 0))
