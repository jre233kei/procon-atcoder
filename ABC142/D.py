from fractions import gcd

ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a, b = nm()

def prime_factorize(n):
    a = set()
    a.add(1)
    while n % 2 == 0:
        a.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.add(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.add(n)
    return a



ps = prime_factorize(gcd(a,b))

print(len(ps))