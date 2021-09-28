# url : https://www.acmicpc.net/problem/1259
# 난이도 : bronze 1

import sys

while True:
    strs = sys.stdin.readline().rstrip()

    if strs == '0':
        break
    elif strs == strs[::-1]:
        print('yes')
    else:
        print('no')