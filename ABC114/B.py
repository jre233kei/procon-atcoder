s = [int(_) for _ in input()]

min_diff = 1000
for i in range(len(s)-2):
    min_diff = min(abs(753-(s[i]*100+s[i+1]*10+s[i+2])),min_diff)

print(min_diff)