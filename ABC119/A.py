s = list(map(int, input().split('/')))

if s[0] < 2019:
    print('Heisei')
elif s[0] > 2019:
    print('TBD')
elif s[1] < 4:
    print('Heisei')
elif s[1] > 4:
    print('TBD')
elif s[2] <= 30:
    print('Heisei')
else:
    print('TBD')