import numpy as np

n = int(input())
s = []

for nn in range(n):
    s.append(sorted(input().encode()))

ans = 0

print(s)
nn = np.array(s)
nnn = np.sort(nn, axis=0)
print(nnn)

s = nnn.tolist()

l = len(s)


cnt = 0
fl = 0

for ss in range(0, l):
    bl = 0
    for sss in range(ss+1, l):
        print("{0} {1}".format(s[ss], s[sss]))
        """
        for ssss in range(10):
            if s[ss][ssss] > s[sss][ssss]:
                bl = 1
                break
        """



        if s[ss] == s[sss]:
            cnt += 1

        else:
            if cnt != 0:
                ans += (cnt+1)/2
                cnt = 0
    print("")


print(round(ans))