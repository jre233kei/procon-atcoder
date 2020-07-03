n, m = map(int, input().split())

ans = [''] * m

cities = []
for i in range(m):
    p, y = map(int, input().split())
    cities.append((p, y, i))

sc = sorted(cities, key=lambda x: x[1])
cities_sorted = sorted(sc, key=lambda x: x[0])


lc = 0
pref_count = 0
city_count = 0
for i in range(m):
    c = cities_sorted[i]

    if c[0] != lc:
        lc = c[0]
        pref_count += 1
        city_count = 0

    city_count += 1

    ans[c[2]] = str(c[0]).zfill(6) + str(city_count).zfill(6)

for i in range(m):
    print(ans[i])
