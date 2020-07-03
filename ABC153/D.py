ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

h = ni()



def atk(n):
  if n==0:
    return 1

  n //=2
  return atk(n)*2

print(atk(h)-1)

