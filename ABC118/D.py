num_to_match = [2, 5, 5, 4, 5, 6, 3, 7, 6]

n, m = map(int, input().split())
a = list(map(int,input().split()))

na = [num_to_match[i-1] for i in a]
sn = sorted(range(len(na)), key=lambda k: na[k])
sa = [a[i] for i in sn]

print(sa)

INF = 10**9


def find(l, summ):
    if summ > n:
        return -INF
    if summ == n:
        return int(''.join([str(li) for li in l]))
    now = 0
    if l:
        now = a.index(l[-1])
    return max(find(l+[ai],summ + num_to_match[ai-1]) for ai in a[:now+2])


print(find([],0))