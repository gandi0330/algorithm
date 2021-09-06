import math

n = int(input())
l = len(str(n))

answer = 0

for i in range(0,l-1):
    answer += 9 * (10 ** i) * (i + 1)

answer += (n - (10**(l-1)) + 1) * l

print(answer)
