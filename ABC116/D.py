from operator import itemgetter

n, k = map(int, input().split())

s = []

last_s = 0
for i in range(n):
    t, d = map(int, input().split())
    s.append((t, d))

ss = sorted(s, key=itemgetter(1), reverse=True)



def calc(l, num, cnt):
    if num == k or cnt == n:
        pts = 0
        kinds = set()

        for li in l:
            if li[0] not in kinds:
                kinds.add(li[0])
            pts += li[1]
        pts += len(kinds) ** 2
        # print(str(l) + ' ' + str(num) + ' ' + str(cnt)+' '+str(pts)+' '+str(kinds)+' '+str(len(kinds)))
        return pts
    return max(calc(l + [ss[cnt]], num + 1, cnt + 1), calc(l, num, cnt + 1))


print(calc([], 0, 0))
