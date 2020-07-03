ni = lambda: int(input())
nm = lambda: map(int, input().split())

a, b = nm()

if a%2==1 and b%2 == 1:
    print('Yes')
else:
    print('No')