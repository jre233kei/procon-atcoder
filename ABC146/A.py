ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

s = input()

if s == 'SUN':
  print(7)
  exit()
print((7 - days.index(s))%7)