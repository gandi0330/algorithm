# url : https://www.acmicpc.net/problem/11054
# 난이도 : gold 3

n = int(input())

num_list = list(map(int,input().split()))

dp1 = [1] * n
dp2 = [1] * n

for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j] :
            dp1[i] = max(dp1[i], dp1[j]+1)


num_list = num_list[::-1]
for i in range(n):
    for j in range(i):
        if num_list[i] > num_list[j] :
            dp2[i] = max(dp2[i], dp2[j]+1)

dp2 = dp2[::-1]

print(max([dp1[i] + dp2[i] for i in range(n)])-1)