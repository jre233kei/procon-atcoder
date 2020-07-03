s = input()

zeros = 0
ones = 0
for i in range(len(s)):
    if s[i] == '0':
        zeros += 1
    if s[i] == '1':
        ones += 1

print(min(zeros,ones)*2)