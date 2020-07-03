n, tt = map(int, input().split())

min_cost = 10000
for i in range(n):
    c, t = map(int, input().split())
    if t <= tt:
        min_cost = min(min_cost, c)

if min_cost < 10000:
    print(min_cost)
else:
    print('TLE')
