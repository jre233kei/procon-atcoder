l,r = map(int, input().split())

lm = l % 2019
rm = r % 2019

ll = min(lm,rm)
rr = max(lm,rm)

min_mod = 9999

for i in range(ll,rr+1):
    for j in range(i+1,rr+1):
        c = (i*j) % 2019
        if c < min_mod:
            min_mod = c

print(min_mod)

