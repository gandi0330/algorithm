# url : https://www.acmicpc.net/problem/13398
# 난이도 : gold 5

n = int(input())

num_list = list(map(int,input().split()))

dp1 = num_list[:]
dp2 = num_list[:]

for i in range(1,n):
    dp1[i] = max(dp1[i], dp1[i-1]+num_list[i])

for i in range(n-2,-1,-1):
    dp2[i] = max(dp2[i], dp2[i+1]+num_list[i])


answer = max(dp1)

for i in range(1,n-1):
    answer = max(answer, dp1[i-1]+dp2[i+1])

print(answer)