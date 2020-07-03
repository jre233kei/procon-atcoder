import numpy as np

n, m = map(int, input().split())
a = np.array(list(map(int, input().split())), dtype='uint64')

for i in range(m):
    b, c = map(int, input().split())
    a = np.append(a, np.full(b, c, dtype='uint64'))

print(np.sum(np.sort(a)[::-1][:n]))
