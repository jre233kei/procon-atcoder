from functools import cmp_to_key

k = int(input())
nn = [int(ni) for ni in input().split()]

goal = (nn[0], nn[1])


def search(n, route):
    if n == goal:
        return route

    def cmptuple(a, b):
        return (abs(nn[0] - b[0]) + abs(nn[1] - b[1])) - (abs(nn[0] - a[0]) + abs(nn[1] - a[1]))

    cands = sorted([(n[0] + a, n[1] + k - a) for a in range(-k, k)], key=cmp_to_key(cmptuple))

    for c in cands:
        search(c, route + [c])


if __name__ == '__main__':
    print(search((0, 0), [(0, 0)]))
