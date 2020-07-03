ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

import sys
sys.setrecursionlimit(10000000)

N,M=nm()


def mod_permutation(n, k, mod):
        if n<=k:
            return 1
        else:
            return (n * mod_permutation(n-1,k,mod))%mod


def mod_combination(n, k, mod):
    # nCk (mod m)
    
    def mod_inv_permutation(k, mod):
        k, mod = int(k), int(mod)
        if k<=1:
            return 1
        else:
            return (pow(k,mod-2,mod) * mod_inv_permutation(k-1, mod))%mod

    return (mod_permutation(n,n-k,mod) * mod_inv_permutation(k, mod))%mod

MOD = 10**9+7
ans = mod_combination(M,N,MOD)*mod_permutation(M,N,MOD)%MOD
print(ans*2)

