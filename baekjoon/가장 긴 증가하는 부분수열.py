# LIS 문제라고도 부른다 Longest Increase Subsequence
# 해결 방법 
# 1. DP
# 2. 완전탐색
# 3. 이진탐색

# DP 풀이

n = int(input())
num_list = list(map(int,input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if num_list[i] >num_list[j]:
            dp[i] = max(dp[j]+1, dp[i])


print(dp[n-1])
