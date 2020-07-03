n = int(input())
s = input()

max_len = 0

zero_fl = 0
last_k = 0
last_j = 0
for i in range(1, (n // 2 + 1)):
    if zero_fl == 1:
        break
    s_closed = set()
    fl = 0
    for j in range(max(0, last_j-1), n - i + 1):
        if fl == 1:
            break
        ss = s[j:j + i]
        if ss in s_closed:
            j += i - 1
            continue
        s_closed.add(ss)
        for k in range(max(j + i, last_k-1), n - i + 1):
            sss = s[k:k + i]
            if ss == sss:
                last_k = k
                last_j = j
                max_len = i
                fl = 1
                break
        if j == n - i:
            zero_fl = 1

print(max_len)
