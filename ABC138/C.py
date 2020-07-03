n = int(input())
v = [int(vi) for vi in input().split()]

vs = sorted(v)

for i in range(n-1):
    vs[i+1] = (vs[i] + vs[i+1])/2

print(vs[n-1])
