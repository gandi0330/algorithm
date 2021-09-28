# url : https://www.acmicpc.net/problem/6603
# 난이도 : silver 2

from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    num_list = list(map(int,input().split()))

    if num_list == [0] :
        break
    else:
        for i in combinations(num_list[1:],6):
            print(' '.join(map(str,i)))
        print()