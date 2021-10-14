# url : https://www.acmicpc.net/problem/4811
# 난이도 : gold 5

import sys, math


while True:
    n = int(sys.stdin.readline())

    if n == 0 :
        break
    else:
        print(math.factorial(2*n) // (math.factorial(n)*math.factorial(n+1)))
