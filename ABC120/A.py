a, b, c = map(int, input().split())

ans = min(c, max(0, b // a))

print(ans)