I = input().split()
A = I[0]
B = I[1]

a = int(A)
b = int(B)

if (a+b)%2 == 0:
    print(round((a+b)/2))
else:
    print("IMPOSSIBLE")
