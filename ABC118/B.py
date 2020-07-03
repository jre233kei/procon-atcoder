n,m = map(int,input().split())

pref = [0] * m
for i in range(n):
    k, *a = map(int,input().split())
    for j in range(k):
        pref[a[j]-1] += 1


print(sum([1 for k in pref if k == n]))
