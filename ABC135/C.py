N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

M = 0

for i in range(N):
    if A[i] <= B[i]:
        m = B[i] - A[i]
        M += A[i]
        if A[i+1] <= m:
            M += A[i+1]
            A[i+1] = 0
        else:
            M += m
            A[i+1] -= m

    else:
        M += B[i]

print(M)