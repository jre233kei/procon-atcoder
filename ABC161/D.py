ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

k = ni()

luns = []


def make_lunlun(l):
    if l > 3234566667:
        return
    luns.append(l)

    last = l-l//10*10

    if last!=0:
        make_lunlun(l*10 + last-1)
    make_lunlun(l*10+last)
    if last!=9:
        make_lunlun(l*10 + last+1)


for i in range(1,10):
    make_lunlun(i)

print(sorted(luns)[k-1])