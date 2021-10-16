import sys


def search(i,j):
    

    if i > 0 and map_[i-1][j] == 1:
        map_[i-1][j] = 0
        search(i-1,j)
    if j > 0 and map_[i][j-1] == 1:
        map_[i][j-1] = 0
        search(i,j-1)
    if i > 0 and j > 0 and  map_[i-1][j-1] == 1:
        map_[i-1][j-1] = 0
        search(i-1,j-1)
    if i > 0 and j < w-1 and map_[i-1][j+1] == 1:
        map_[i-1][j+1] = 0
        search(i-1,j+1)
    if i < h-1 and j > 0 and map_[i+1][j-1] == 1:
        map_[i+1][j-1] = 0
        search(i+1,j-1)
    if i < h-1 and j < w-1 and map_[i+1][j+1] == 1:
        map_[i+1][j+1] = 0
        search(i-1,j)
    if i < h-1 and map_[i+1][j] == 1:
        map_[i+1][j] = 0
        search(i+1,j)
    if j < w-1 and map_[i][j+1] == 1:
        map_[i][j+1] = 0
        search(i,j+1)
    



while True:
    w,h = map(int,sys.stdin.readline().split())

    if w == 0 and h == 0 :
        break

    
    map_ = [[*map(int,sys.stdin.readline().split())] for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if map_[i][j] == 1:
                map_[i][j] = 0
                cnt += 1
                search(i,j)
    
    print(cnt)

