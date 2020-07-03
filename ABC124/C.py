s = [int(i) for i in input()]
cnt = 0
for i in range(len(s) - 1):
    if s[i] == 0 and s[i + 1] == 0:
        s[i + 1] = 1
        cnt += 1
    elif s[i] == 1 and s[i + 1] == 1:
        s[i + 1] = 0
        cnt += 1
print(cnt)
