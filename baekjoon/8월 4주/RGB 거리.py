# url : https://www.acmicpc.net/problem/1149
# 난이도 : silver 1

import sys
n = int(input())

num_lists = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]


# 이 전에 칠한 색을 제외한 비용 중 작은 값을 현재 비용과 더한다
for i in range(1, len(num_lists)):
    num_lists[i][0] += min(num_lists[i-1][1],num_lists[i-1][2])
    num_lists[i][1] += min(num_lists[i-1][0],num_lists[i-1][2])
    num_lists[i][2] += min(num_lists[i-1][0],num_lists[i-1][1])

print(min(num_lists[n-1]))
print(num_lists)