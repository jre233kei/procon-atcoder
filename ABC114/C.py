import sys

n = int(input())
sys.setrecursionlimit(2*10**9+1)


def count(num):
    if num > n:
        return 0
    fl = 0
    s = str(num)
    if '3' in s and '5' in s and '7' in s:
        fl = 1

    return fl + count(num*10+3) + count(num*10+5) + count(num*10+7)


print(count(0))