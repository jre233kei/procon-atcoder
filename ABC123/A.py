a = []
for i in range(5):
    a.append(int(input()))
k = int(input())
fl = 0
for i in range(5):
    for j in range(i,5):
        if a[j] - a[i] > k:
            fl = 1

if fl == 1:
    print(':(')
else:
    print('Yay!')