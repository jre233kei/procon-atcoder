import sys

sys.setrecursionlimit(2001 * 2001)

h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append([si for si in input()])

max_light = 0


def search(x, y, dir):
    if x < 0 or y < 0 or y >= h or x >= w:
        return 0
    if s[y][x] == '#':
        return 0
    if dir == 0:
        return 1 + search(x, y - 1, dir)
    if dir == 1:
        return 1 + search(x + 1, y, dir)
    if dir == 2:
        return 1 + search(x, y + 1, dir)
    if dir == 3:
        return 1 + search(x - 1, y, dir)


def light_search_hol(x, y):
    return search(x, y, 1) + search(x, y, 3)


def light_search_ver(x, y):
    return search(x, y, 0) + search(x, y, 2)


last_hol = 0
last_ver = 0
for i in range(w):
    for j in range(h):
        # hol = 0
        ver = 0
        # hol_fl = 0
        ver_fl = 0
        """
        if i > 1:
            if s[j][i - 1] == '.':
                hol_fl = 1
                hol = last_hol
        """
        if j > 1:
            if s[j - 1][i] == '.':
                ver_fl = 1
                ver = last_ver
        """
        if hol_fl == 0:
            hol = light_search_hol(i, j)
            last_hol = hol
        """
        if ver_fl == 0:
            ver = light_search_ver(i, j)
            last_ver = ver
        hol = light_search_hol(i, j)
        if hol + ver > max_light:
            max_light = hol + ver
            # print('{0} {1}'.format(i, j))

print(max_light-3)
