# url : https://www.acmicpc.net/problem/9465
# 난이도 : silver 2


import sys

t  = int(input())

for _ in range(t):
    n = int(sys.stdin.readline())

    up_case = [0] + list(map(int,sys.stdin.readline().split()))
    down_case = [0] + list(map(int,sys.stdin.readline().split()))

    up_dp = [0] * (n+1)
    down_dp = [0] * (n+1)
    
    up_dp[1] = up_case[1]
    down_dp[1] = down_case[1]

    for i in range(2,n+1):
        up_dp[i] = max(down_dp[i-1] + up_case[i], max(up_dp[i-2],down_dp[i-2]) + up_case[i])
        down_dp[i] = max(up_dp[i-1] + down_case[i], max(up_dp[i-2],down_dp[i-2]) + down_case[i])
    
    print(max(up_dp[n], down_dp[n]))
