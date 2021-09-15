# url : https://www.acmicpc.net/problem/2133
# 난이도 : silver 1

num = int(input())

dp = [0] * 31

dp[2] = 3

for n in range(4, num+1, 2):
    
    dp[n] += dp[n-2] * 3
    dp[n] += sum([dp[j] for j in range(2, n-2, 2)]) * 2
    dp[n] += 2

print(dp[num])