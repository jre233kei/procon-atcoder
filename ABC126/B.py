ym = 0
my = 0

s = input()

hi = int(s[2:])
lo = int(s[:2])


def isym(l):
    if l == 0:
        return False
    if l <= 12:
        return True
    else:
        return False


ym = 0
my = 0
if isym(hi):
    ym = 1
if isym(lo):
    my = 1

if ym == 1 and my == 1:
    print('AMBIGUOUS')
if ym == 1 and my == 0:
    print('YYMM')
if ym == 0 and my == 1:
    print('MMYY')
if ym == 0 and my == 0:
    print('NA')
