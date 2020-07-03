s = input()

bad = 0
for i in range(1,4):
    if s[i] == s[i-1]:
        print('Bad')
        bad = 1
        break
if bad==0:
    print('Good')