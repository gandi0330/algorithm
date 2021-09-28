# from itertools import product

# n,k = map(int, input().split())

# cnt = 0
# for tp in [*product([i for i in range(n+1)], repeat=k)]:
#     if sum(tp) == n :
#         cnt += 1

# print(cnt)

n, k = map(int, input().split())

dp = [[1]*(n+1) for _ in range(k)]

for i in range(1, k):
    for j in range(n+1):
        for l in range(j):
            dp[i][j] += dp[i-1][j-l]

print(dp[k-1][n] % 1000000000)