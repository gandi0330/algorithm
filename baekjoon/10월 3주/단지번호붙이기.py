# url : https://www.acmicpc.net/problem/2667
# 난이도 : silver 1

import sys

def search(i,j):
    global house
    if i < n-1 and map[i+1][j] == 1:
        house += 1
        map[i+1][j] = 0
        search(i+1,j)
    if j < n-1 and map[i][j+1] == 1:
        house += 1
        map[i][j+1] = 0
        search(i,j+1)
    if i > 0 and map[i-1][j] == 1:
        house += 1
        map[i-1][j] = 0
        search(i-1,j)
    if j > 0 and map[i][j-1] == 1:
        house += 1
        map[i][j-1] = 0
        search(i,j-1)

n = int(input())

map = [[ int(i) for i in sys.stdin.readline().rstrip()] for _ in range(n)]

answer = []
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            map[i][j] = 0
            house = 1
            search(i,j)
            answer.append(house)


print(len(answer))

for i in sorted(answer):
    print(i)

