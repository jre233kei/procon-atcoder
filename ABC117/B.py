n = int(input())
l = list(map(int, input().split()))

sl = sorted(l)

if sl[-1] < sum(sl[:-1]):
    print('Yes')
else:
    print('No')