X = input().split()
A = int(X[0])
B = int(X[1])

ans = -999999999

a = []

a.append(A+B)
a.append(A-B)
a.append(A*B)

add = A+B
sub = A-B
mul = A*B

if add > ans:
    ans = add

if sub > ans:
    ans =sub

if mul > ans:
    ans = mul

print(ans)