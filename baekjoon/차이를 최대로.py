# url : https://www.acmicpc.net/problem/10819
# 난이도 : silver 2

from itertools import permutations

n = int(input())

num_list = list(map(int,input().split()))

answer = -800

for i in permutations(num_list, n):
    sub = 0
    for j in range(len(i)-1):
        sub += abs(i[j] - i[j+1])
    
    answer = max(answer, sub)

print(answer)