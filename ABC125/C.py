from fractions import gcd
from functools import reduce


def find_gcd(list_):
    x = reduce(gcd, list_)
    return x


n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    a_ = a.copy()
    a_.pop(i)
    ans = max(ans, find_gcd(a_))
print(ans)