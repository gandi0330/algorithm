# url : https://www.acmicpc.net/problem/13023
# 난이도 : gold 5

import sys
sys.setrecursionlimit(10**6) # 백준 재귀제한 해제

n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n)]

visited = [False]* n
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)


switch = False # 깊이가 5 이상일 때 켜지는 변수
def dfs(node,depth,visited):
    
    global switch
	
    # 깊이가 5 이상일 때 switch를 키고 리턴한다
    if depth >= 5:
        switch = True
        return
    

    
    for i in graph[node]:
        if visited[i] == False:
            visited[node] = True
            dfs(i,depth+1,visited)
            visited[node] = False

# 모든 정점에 대해 검색한다
for i in range(n):
    visited[i] = True
    dfs(i,1,visited)
    visited[i] = False
	
    # 스위치가 켜져있으면 1을 출력하고 멈춘다
    if switch == True :
        print(1)
        break

# 모든 정점을 검색해도 스위치가 켜져있지 않았다면 0을 출력한다
else:
    print(0)




