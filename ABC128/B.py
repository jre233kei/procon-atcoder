n = int(input())

city_pts = {}
cities = set()

for i in range(n):
    city, pts_raw = input().split()
    pts = int(pts_raw)

    if city in cities:
        city_pts[city].append((pts,i))
    else:
        city_pts[city] = [(pts,i)]

    cities.add(city)

for c in sorted(cities):
    pts = city_pts[c]

    for p in sorted(pts,reverse=True):
        print(p[1]+1)


