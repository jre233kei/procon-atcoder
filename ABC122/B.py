s = input()

ans = 0
for i in range(len(s)+1):
    for j in range(len(s)+1):
        ss = s[i:j]
        acgt = ['A', 'C', 'G', 'T']
        fl = 1
        for si in ss:
            if si not in acgt:
                fl = 0
                break
        if fl == 1 and len(ss) > 0:
            ans = max(ans, j - i)

print(ans)
