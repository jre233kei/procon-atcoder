X = input().split()
k = int(X[0])
x = int(X[1])

print(x-k+1, end='')
for i in range(x-k+2,x+k):
    print(' ',end='')
    print(i,end='')