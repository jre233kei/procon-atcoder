import sys
sys.setrecursionlimit(2*10**5+2)

n = int(input())
a = list(map(int, input().split()))

ans = []


def ball_ok(balls):
    global ans
    for i in range(1, n + 1):
        sum_ = 0
        for j in range(i, n + 1, i):

            sum_ += balls[j]

        if sum_ % 2 != a[i-1]:
            return 0

    ans = balls
    return 1


def ball(balls, k):
    if k == n+1:
        return ball_ok(balls)
    b0 = ball(balls + [0], k + 1)
    b1 = ball(balls + [1], k + 1)
    return b0 or b1


res = ball(balls=[1], k=1)

cnt = 0

ansi = []

for i in range(1, len(ans)):
    if ans[i] == 1:
        cnt += 1
        ansi.append(i)

if cnt == 0:
    print(0)
else:
    print(len(ansi))
    for _ in ansi:
        print(_)