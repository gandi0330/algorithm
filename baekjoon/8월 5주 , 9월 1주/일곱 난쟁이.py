# url : https://www.acmicpc.net/problem/2309
# 난이도 : bronze 2

from itertools import combinations

num_list = [int(input()) for _ in range(9)]

for i in combinations(num_list,7) :
    if sum(i) == 100 :
        for j in sorted(i):
            print(j)

        break 