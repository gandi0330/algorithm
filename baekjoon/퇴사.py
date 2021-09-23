# url : https://www.acmicpc.net/problem/14501
# 난이도 : silver 3

import sys

input = sys.stdin.readline
n = int(input())

consult_list = [[0,0]] + [list(map(int,input().split())) for _ in range(n)]

dp = [0] * (n+1)

for i in range(1,n+1):
    dp[i] = dp[i-1]
    for j in range(1,i+1):
        if  i - j + 1 == consult_list[j][0] :
            dp[i] = max(dp[i], consult_list[j][1] + dp[j-1])


print(dp[-1])