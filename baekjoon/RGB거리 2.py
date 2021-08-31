import sys

n = int(input())

rgb_list = [[0,0,0]] + [list(map(int,sys.stdin.readline().split())) for _ in range(n)]



for i in range(3,n+1):
    rgb_list[i][0] += min(rgb_list[i-1][1], rgb_list[i-1][2])
    rgb_list[i][1] += min(rgb_list[i-1][0], rgb_list[i-1][2])
    rgb_list[i][2] += min(rgb_list[i-1][0], rgb_list[i-1][1])


rgb_list[n][0] += min(rgb_list[1][1], rgb_list[1][2])
rgb_list[n][1] += min(rgb_list[1][0], rgb_list[1][2])
rgb_list[n][2] += min(rgb_list[1][0], rgb_list[1][1])

print(min(rgb_list[n]))