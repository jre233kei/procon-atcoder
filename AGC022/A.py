ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

s = input()

if s == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
    exit()

L = 26
s = [ord(c) - ord('a') for c in s]

memo = [False] * L
for c in s:
    memo[c] = True

lowerbound = 0
while all(memo[lowerbound:]):
    c = s.pop()
    lowerbound = c + 1
    memo[c] = False

for i in range(lowerbound, L):
    if not memo[i]:
        s.append(i)
        break

print(''.join(map(chr, [c + ord('a') for c in s])))
