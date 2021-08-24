# url : https://www.acmicpc.net/problem/11055
# 난이도 : silver 2

n = int(input())
num_list = list(map(int,input().split()))

dp = [0]* n


for i in range(n):
    dp[i] = num_list[i] + max([0] + [dp[j] for j in range(0,i) if num_list[i] > num_list[j]])

print(max(dp))