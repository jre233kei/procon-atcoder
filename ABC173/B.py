ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n=ni()

j = dict()
j['AC']=0
j['WA']=0
j['TLE']=0
j['RE']=0
for i in range(n):
  s=input()
  j[s]+=1

print('AC x {}'.format(j['AC']))
print('WA x {}'.format(j['WA']))
print('TLE x {}'.format(j['TLE']))
print('RE x {}'.format(j['RE']))
