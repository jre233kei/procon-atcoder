s = int(input())

log = set()
log.add(s)
for i in range(1001000):
    if s%2==0:
        s //=2
    else:
        s = 3*s+1

    if s in log:
        print(i+2)
        break

    log.add(s)