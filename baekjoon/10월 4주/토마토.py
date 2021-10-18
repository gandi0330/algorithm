# url : https://www.acmicpc.net/problem/7576
# 난이도 : silver 1

import sys
from collections import deque

m,n = map(int,sys.stdin.readline().split())

mat = [[*map(int,sys.stdin.readline().split())] for _ in range(n)]



ripe_tomatoes = []

for i in range(n):
    for j in range(m):
        if mat[i][j] == 1:
            ripe_tomatoes.append([i,j,0])


x_case = [1,0,-1,0]
y_case = [0,-1,0,1]

q = deque(ripe_tomatoes)


while q:
    x,y,d = map(int,q.popleft())
    for i in range(4):
        if 0<=x+x_case[i]<n and 0<=y+y_case[i]<m and mat[x+x_case[i]][y+y_case[i]] == 0:
            mat[x+x_case[i]][y+y_case[i]] = 1
            q.append([x+x_case[i],y+y_case[i],d+1])


for i in range(n):
    if 0 in mat[i]:
        print(-1)
        break
else:
    print(d)