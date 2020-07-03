n = int(input())
w = list(map(int, input().split()))

mindiff = 999999

s1 = 0
s2 = sum(w)

for i in range(n):
    mindiff = min(mindiff, abs(s2 - s1))
    s1 += w[i]
    s2 -= w[i]

print(mindiff)
