import math

n, d = map(int, input().split())

def dist(x,y):
    ans = 0
    for i in range(d):
        ans += (x[i] - y[i])**2
    return math.sqrt(ans)

points = []
for i in range(n):
    points.append(list(map(int, input().split())))


cnt = 0
for i in range(n):
    for j in range(i+1,n):
        if dist(points[i],points[j]).is_integer():
            cnt += 1

print(cnt)