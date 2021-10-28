import sys
N,M = map(int,sys.stdin.readline().split())

mat = [[i for i in sys.stdin.readline().strip()] for _ in range(N)]


n = [0,-1,0,1]
m = [1,0,-1,0]

def dfs(node_n,node_m,depth):
    
    global start, cycle
    visited[node_n][node_m] = True

    for i in range(4):
        if 0<=n[i]+node_n<N and 0<=m[i]+node_m<M and mat[node_n][node_m] == mat[n[i]+node_n][m[i]+node_m] :
            if visited[n[i]+node_n][m[i]+node_m] == False:
                dfs(n[i]+node_n,m[i]+node_m,depth+1)
            elif depth >= 4 and start[0] == n[i]+node_n and start[1] == m[i]+node_m:
                cycle = True
                return

answer = 'No'
cycle = False
for i in range(N):
    for j in range(M):
        visited = [[False for _ in range(M)] for _ in range(N)]
        
            
        start = [i,j]
        dfs(i,j,1)

        if cycle == True:
            answer = 'Yes'
            break


print(answer)