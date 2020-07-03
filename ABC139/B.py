a, b = map(int, input().split())

plgcnt = 0
tapcnt = 1

flg=0

while(True):
    if tapcnt >= b:
        print(plgcnt)
        break
    tapcnt += a - 1
    plgcnt += 1
