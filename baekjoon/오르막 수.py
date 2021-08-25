n = int(input())

d = [1] * 10

for _ in range(2, n+1):
    for i in range(0,10):
        d[i] = sum(d[i:])

print(sum(d))
print(d)