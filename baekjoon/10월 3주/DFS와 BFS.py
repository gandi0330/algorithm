import sys
from collections import deque 

matrix = [[[0] for _ in range(1001)] for _ in range(1001)]
n,m,v = map(int,sys.stdin.readline().split())
visited_dfs = [False] * 1001
visited_bfs = [False] * 1001
dfs_list = []
bfs_list = []

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    matrix[a][b] = 1
    matrix[b][a] = 1


def dfs(node):
    dfs_list.append(node)
    visited_dfs[node] = True

    for i in range(1,n+1):
        if visited_dfs[i] == False and matrix[node][i] == 1 :
            dfs(i)
    

def bfs(node):
    visited_bfs[node] = True
    q = deque()

    q.append(node)

    while q :
        V = q.popleft()
        bfs_list.append(V)
       
        for i in range(1,n+1):
            if visited_bfs[i] == False and matrix[V][i] == 1 :
                visited_bfs[i] = True
                q.append(i)

dfs(v)
print(*dfs_list)

bfs(v)
print(*bfs_list)

