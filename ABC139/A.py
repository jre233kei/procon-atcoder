s = [si for si in input()]
t = [ti for ti in input()]


cnt = 0
for i in range(3):
    if s[i] == t[i]:
        cnt += 1

print(cnt)

