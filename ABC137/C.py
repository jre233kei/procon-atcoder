n = int(input())
sraw = dict()

for nn in range(n):
    i = "".join(sorted(input()))
    if i in sraw:
        sraw[i] += 1
    else:
        sraw[i] = 1

ans = 0

for ss in sraw:
    ans += round(sraw[ss]*(sraw[ss]-1)/2)

print(ans)
