import sys

n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n)]

visited = [False]* n
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)


switch = False
def dfs(node,depth):
    
    global switch
    print(depth)
    if depth >= 5:
        switch = True
    visited[node] = True

    
    for i in graph[node]:
        if visited[i] == False:
            dfs(i,depth+1)


for i in range(n):
    if visited[i] == False:
        
        dfs(i,1)


if switch == True:
    print(1)
else:
    print(0)

