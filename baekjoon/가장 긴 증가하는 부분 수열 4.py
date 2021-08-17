# LIS 문제라고도 부른다 Longest Increase Subsequence

# DP 풀이

n = int(input())
num_list = list(map(int,input().split()))
dict_dp = {}
dp1 = [1] * n
dp2 = [-1] * n

for i in range(1, n):
    for j in range(i):
        if num_list[i] > num_list[j] and dp1[i] < dp1[j] + 1:
            dp1[i] = dp1[j] + 1
            dp2[i] = j

print(max(dp1))

answer = []
idx = dp1.index(max(dp1))
while idx != -1:
    answer.append(num_list[idx])

    idx = dp2[idx]

print(' '.join(map(str,answer)))
