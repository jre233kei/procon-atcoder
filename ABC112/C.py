n = int(input())

pts = []

for i in range(n):
    x, y, h = map(int, input().split())
    pts.append((x, y, h))

for y in range(101):
    for x in range(101):
        needH = -1
        for i in range(n):
            tmp = pts[i][2] + abs(y - pts[i][1]) + abs(x - pts[i][0])
            if needH == -1:
                needH = tmp
            else:
                if needH != tmp:
                    needH = -2
                    break
        if needH == -2:
            continue

        for i in range(n):
            if pts[i][2] == 0:
                dist = abs(y - pts[i][1]) + abs(x - pts[i][0])
                if needH > dist:
                    needH = -2
                    break

        if needH == -2:
            continue

        print('{0} {1} {2}'.format(x, y, needH))
        exit()
