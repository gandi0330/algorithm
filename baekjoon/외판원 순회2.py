# url : https://www.acmicpc.net/problem/10971
# 난이도 : silver 2

import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())

matrix = [list(map(int,input().split())) for _ in range(n)]
answer = 10000000
for i in permutations(range(1,n),n-1):
    num_list = [*i]
    num_list = [0] + num_list + [0]

    print(num_list)
    sub = 0
    for j in range(n) :
        cost = matrix[num_list[j]-1][num_list[j+1]-1]
        if cost == 0 :
            break
        else :
            sub += cost
        if sub > answer :
            break
    
    else:
        if answer > sub:
            answer = sub
print(answer)