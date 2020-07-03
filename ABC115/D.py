n,x = map(int, input().split())

b = ['P']

for i in range(n+1):
    b.append('B'+b[i-1]+'P'+b[i-1]+'B')

ans = 0
for bi in b[n+1][:x]:
    if bi == 'P':
        ans += 1

print(ans)