n, k = map(int, input().split())
s = [si for si in input()]


def hn(lst):
    cnt = 0
    for i in range(0, n):
        if lst[i] == 'L':
            if i > 0:
                if lst[i - 1] == 'L':
                    cnt += 1
        else:
            if i < n - 1:
                if lst[i + 1] == 'R':
                    cnt += 1
    return cnt, lst


def op(lst, l, r):
    nlst = [li for li in lst]

    for i in range(0, r - l + 1):
        if lst[l + i - 1] == 'L':
            nlst[r - i - 1] = 'R'

        else:
            nlst[r - i - 1] = 'L'

    return nlst


def tryop(best, lst, cnt):
    if cnt >= k:
        print(best)
        return best

    for i in range(1, n):
        for j in range(i, n):
            res = hn(op(lst, i, j))
            if res[0] > best:
                best = res[0]
                best_res = res[1]

    tryop(best, best_res, cnt + 1)


tryop(0, lst=s, cnt=0)
