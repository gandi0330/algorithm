# url : https://www.acmicpc.net/problem/2178
# 난이도 : silver 1

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

mat = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(n)]

x_case = [1,0,-1,0]
y_case = [0,-1,0,1]



q = deque()

q.append([0,0,1])
mat[0][0] = 0
while q:
    x,y,d = map(int,q.popleft())

    if x == n-1 and y == m-1 :
        print(d)
        break

    for i in range(4):
        if 0<=x+x_case[i]<n and 0<=y+y_case[i]<m and mat[x+x_case[i]][y+y_case[i]] == 1:
            mat[x+x_case[i]][y+y_case[i]] = 0
            q.append([x+x_case[i],y+y_case[i],d+1])