import sys

n,m = map(int,sys.stdin.readline().split())

visited = [False] * (n+1)

graph = [[] for _ in range(n)] + [[]]

for i in range(m):
    u,v = map(int,sys.stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)


def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if visited[i] == False:
            dfs(i)

compo_cnt = 0

for i in range(1,n+1):
    if visited[i] == False:
        compo_cnt += 1
        dfs(i)

print(compo_cnt)