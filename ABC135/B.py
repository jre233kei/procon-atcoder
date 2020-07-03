N = int(input())
P = [int(p) for p in input().split()]


for i in range(N-1):
    if P[i] > P[i+1]:
        tmp = P[P[i]-1]
        P[P[i]-1] = P[i]
        P[i] = tmp
        break

if P == sorted(P):
    print('YES')
else:
    print('NO')



