n = int(input())
num_list = list(map(int,input().split()))

dp = num_list[:]


for i in range(n):
    dp[i] = num_list[i] + max([0] + [dp[j] for j in range(0,i) if num_list[i] > num_list[j]])

print(max(dp)