import math

time = 0
diff = 0
for i in range(5):
    t = int(input())
    tt = math.ceil(t / 10) * 10
    time += tt
    diff = max(diff, tt-t)
print(time - diff)
