# url : https://www.acmicpc.net/problem/3085
# 난이도 : silver 4 ????

import sys

n = int(input())

candy = [[*sys.stdin.readline().strip()] for _ in range(n)]

answer = 0

def h():
    global answer, n, candy

    for i in range(n):
        sub = 1
        for j in range(n-1):
            if candy[j][i] == candy[j+1][i] :
                sub += 1
            else:
                if answer < sub :
                    answer = sub
                sub = 1

        if answer < sub:
            answer = sub

def w():
    global answer, n, candy

    for i in range(n):
        sub = 1
        for j in range(n-1):
            if candy[i][j] == candy[i][j+1]:
                sub += 1
            else :
                if answer < sub :
                    answer = sub
                sub = 1
        
        if answer < sub:
            answer = sub

for i in range(n):
    for j in range(n):
        if j < n-1 :
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            h()
            w()
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        if i < n-1:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            h()
            w()
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]


print(answer)