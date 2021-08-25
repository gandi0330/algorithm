import sys

n = int(input())



dp = [0] * 10001

wine_list = [0] + [int(sys.stdin.readline()) for _ in range(n)]

dp[1] = wine_list[1]

if n >= 2 :
    dp[2] = wine_list[1] + wine_list[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-3] + wine_list[i-1] + wine_list[i], dp[i-2] + wine_list[i], dp[i-1])

print(dp[n])