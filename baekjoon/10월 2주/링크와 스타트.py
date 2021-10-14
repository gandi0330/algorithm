# url : https://www.acmicpc.net/problem/14889
# 난이도 : silver 1
import sys

input = sys.stdin.readline

n = int(input())

matrix = [list(map(int,input().split())) for _ in range(n)]

visited= [False] * n

min_list= []

def recur(target,start,link):

    if target == n:
        min_list.append(abs(start-link))
        return


    visited[target] = True
    recur(target+1, start + sum([matrix[target][i] + matrix[i][target] for i in range(target) if visited[i] == True]), link)
    visited[target] = False
    recur(target+1, start,  link + sum([matrix[target][i] +matrix[i][target] for i in range(target) if visited[i] == False]))
            
recur(0,0,0)

print(min(min_list))
