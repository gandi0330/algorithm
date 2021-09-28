# url : https://www.acmicpc.net/problem/17404
# 난이도 : gold 4

import sys

n = int(input())

rgb_list = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

min_val = 1000001

for color in range(3):
    dp = [[0,0,0] for _ in range(n)]
    
    for i in range(3):
        if color == i:
            dp[0][i] = rgb_list[0][color]
        else:
            dp[0][i] = 1000001
    

    for i in range(1,n):
        dp[i][0] += rgb_list[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] += rgb_list[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] += rgb_list[i][2] + min(dp[i-1][0], dp[i-1][1])

    

    for i in range(3):
        if i == color : continue
        min_val = min(dp[n-1][i], min_val)

   

print(min_val)