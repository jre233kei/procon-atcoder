n, l = map(int,input().split())

sum_taste = 0
min_abs = 999
idx = -1
for i in range(n):
    taste = l+i
    if min_abs > abs(taste):
        min_abs = abs(taste)
        idx = i
    sum_taste += taste

print(sum_taste - (l+idx))