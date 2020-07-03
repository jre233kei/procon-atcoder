n, k = map(int, input().split())

s = input()

for i in range(n):
    if i == k-1:
        print(s[i].lower(), end='')
        continue
    print(s[i], end='')
