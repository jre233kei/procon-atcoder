r, d, x_2000 = map(int,input().split())

for i in range(2,12):
    print(round((x_2000-d/(r-1))*r**(i-1)+d/(r-1)))