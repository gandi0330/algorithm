import sys

t = int(input())

dp = [0] * (1000001)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(t):
    num = int(sys.stdin.readline())

    for i in range(4,num+1):
        if dp[i] == 0 :
            dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009

    print(dp[num])

