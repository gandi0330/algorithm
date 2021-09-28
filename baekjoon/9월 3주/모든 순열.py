# url : https://www.acmicpc.net/problem/10974
# 난이도 : silver 3

from itertools import permutations

n = int(input())

for i in permutations(range(1,n+1),n):
    print(*i)