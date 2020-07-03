from collections import Counter

n = int(input())

v = list(map(int, input().split()))

odds = []
evens = []

for i in range(n):
    if i % 2 == 0:
        evens.append(v[i])
    else:
        odds.append(v[i])

evens_c = Counter(evens).most_common(2)
odds_c = Counter(odds).most_common(2)

if evens_c[0][0] != odds_c[0][0]:
    print(n - evens_c[0][1] - odds_c[0][1])
    exit()

if len(evens_c) == 1 or len(odds_c) == 1:
    print(n // 2)
    exit()

print(n - max(evens_c[0][1] + odds_c[1][1], evens_c[1][1] + odds_c[0][1]))
