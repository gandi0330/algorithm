n = int(input())

d = [0,1,1,1,1,1,1,1,1,1]

for _ in range(1, n):
    sub_d = [0]*10
    sub_d[0] = d[1]
    sub_d[9] = d[8]
    for idx in range(1,9):
        sub_d[idx] = d[idx-1] + d[idx+1]

    d = sub_d
print(sum(d)%1000000000)

