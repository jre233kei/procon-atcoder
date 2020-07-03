odds = ['R','U','D']
evens = ['L','U','D']

s = input()

fl = 0
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] not in odds:
            fl = 1
            break
    if i % 2 == 1:
        if s[i] not in evens:
            fl = 1
            break

if fl == 0:
    print('Yes')
else:
    print('No')