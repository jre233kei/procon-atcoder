from fractions import gcd

a, b, c, d = map(int, input().split())


def lcm(x, y):
    if gcd(x, y) == 0:
        return x * y
    return x * y // gcd(x, y)


def cantdiv(x):
    return x - x // c - x // d + x // lcm(c, d)


print(cantdiv(b) - cantdiv(a - 1))
