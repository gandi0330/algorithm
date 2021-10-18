# url : https://www.acmicpc.net/problem/7562
# 난이도 : silver 2

import sys
from collections import deque

tc = int(sys.stdin.readline())

case_x = [1,2,2,1,-1,-2,-2,-1]
case_y = [2,1,-1,-2,-2,-1,1,2]

for _ in range(tc):
    l = int(sys.stdin.readline())
    now_x, now_y = map(int,sys.stdin.readline().split())
    target_x, target_y = map(int,sys.stdin.readline().split())

    q = deque()

    visited = [[0 for _ in range(l)] for _ in range(l)]

    visited[now_x][now_y] = 1

    q.append([now_x,now_y,0])

    while q:
        x,y,d = map(int,q.popleft())
        
        if x == target_x and y == target_y :
            print(d)
            break

        for i in range(8):
            if 0 <= x+case_x[i] < l and 0 <= y+case_y[i] < l and visited[x+case_x[i]][y+case_y[i]] == 0:
                visited[x+case_x[i]][y+case_y[i]] = 1
                q.append([x+case_x[i],y+case_y[i],d+1])
