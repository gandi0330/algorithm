# url : https://www.acmicpc.net/problem/6064
# 난이도 : silver 1

import sys

n = int(input())

for _ in range(n):
    M,N,x,y = map(int, sys.stdin.readline().split())

    m = (x - 1) % N + 1
    n = x
    year = x

    while True:
        if n == y :
            print(year)
            break
        elif year > M*N :
            print(-1)
            break
        else :
            n = (n + M - 1) % N + 1
            year += M
        
        