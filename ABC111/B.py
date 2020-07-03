n = int(input())

z = []
for i in range(1, 10):
    z.append(i * 100 + i * 10 + i)

for zi in z:
    if zi >= n:
        print(zi)
        exit()