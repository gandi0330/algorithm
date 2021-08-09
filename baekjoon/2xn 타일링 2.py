num = int(input())

d = [0] * (num+1)

d[0] = 1
d[1] = 3

for i  in range(2,num):
    d[i] = d[i-1] + d[i-2]  * 2

print(d[num-1])