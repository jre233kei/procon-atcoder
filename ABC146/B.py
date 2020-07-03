ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
s = input()

for si in s:
  os = ord(si)
  print(chr(((os+n)-ord('A'))%26+ord('A')),end="")