w, h, x, y = map(int, input().split())

mulans = 0
if h == 2 * y and w == 2 * x:
    mulans = 1

ans = w * h / 2

print(str(ans) + ' ' + str(mulans))
