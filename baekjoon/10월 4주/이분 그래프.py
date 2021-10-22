# url : https://www.acmicpc.net/problem/1707
# 난이도 : gold 4

import sys
sys.setrecursionlimit(10**6) # 백준 재귀제한 해제

tc = int(input())

def dfs(node,color):

    global answer

    visited[node] = color
    for i in graph[node]:
        if visited[i] == 0 :
            dfs(i,-color)
        elif visited[i] == -color:
            pass
        else:
            answer = "NO"
            return


for _ in range(tc):
    V,E = map(int,sys.stdin.readline().split())

    graph = [[] for _ in range(V)]
    answer = "YES"
    for _ in range(E):
        u,v = map(int,sys.stdin.readline().split())

        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    visited = [0] * V

    for i in range(V):
        if visited[i] == 0 : 
            dfs(i,1)

    print(answer)

