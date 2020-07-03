from functools import reduce

a, b = map(int, input().split())

aa = [i for i in range(a, b + 1)]


def xor(x, y):
    return x ^ y


print(reduce(xor, aa))
