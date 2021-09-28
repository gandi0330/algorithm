# url : https://www.acmicpc.net/problem/9461
# 난이도 : silver 3

import sys

tc = int(input())

for _ in range(tc):
    n = int(sys.stdin.readline())

    if n < 4 :
        print(1)
    else:
        dp = [1] * n

        for i in range(3, n):
            dp[i] = dp[i-2] + dp[i-3]
        
        print(dp[-1])